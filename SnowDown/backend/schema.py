import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
import jwt
from django.conf import settings
import datetime
import hashlib

from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphql_jwt.utils import get_payload
from graphql_jwt.decorators import token_auth
from .models import Animal_Table, SubAnimal_Table, Animal_Characteristics_Table, Incident_Photos_Table, Incident_Table, Incident_Before_Photos_Table,\
    Incident_After_Photos_Table, Group_Incident_Table, TokenIssued
from graphql_jwt.decorators import login_required, superuser_required



class User_Info(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "Last_name", 'email', "Volunteer", "Picture", "is_active", "is_superuser")
        
class CreateUser(graphene.Mutation):
    user = graphene.Field(User_Info)
    
    class Arguments:
            firstName = graphene.String(required=True)
            lastName = graphene.String(required=True)
            email = graphene.String(required=True)
            password = graphene.String(required=True)
            Picture = graphene.String(required=True)
            Volunteer = graphene.Boolean(required=True)
            isActive = graphene.Boolean(required=True)
            isSuperuser = graphene.Boolean(required=True)
            Token = graphene.String(required=True)
            
    def mutate(self, info, firstName, lastName, email, Picture, Volunteer, password, isActive, isSuperuser, Token):
        value = hashlib.sha256(Token.encode('utf-8')).hexdigest()
        try:
            if TokenIssued.objects.filter(token=value).count() > 0:
                TokenIssued.objects.get(token=value).delete()
                data = jwt.decode(Token, settings.SECRET_KEY, algorithms=["HS256"])
                if data['Purpose'] == 'Creating an account':
                    user = get_user_model()(
                        email = email,
                        first_name=firstName,
                        Last_name=lastName,
                        Picture=Picture,
                        Volunteer=Volunteer,
                        is_active=isActive,
                        is_superuser=isSuperuser,
                    )
                    user.set_password(password)
                    user.save()
                    print('yes')
                    return CreateUser(user=user)
                else:
                    raise GraphQLError('Token is not verified')
            else:
                raise GraphQLError('Token is not Valid')
        except jwt.ExpiredSignatureError:
            raise GraphQLError('Token is not verified')
        
class PasswordReset(graphene.Mutation):
    State = graphene.String()
    
    class Arguments:
        password = graphene.String(required=True)
        token = graphene.String(required=True)
        
    def mutate(self, info, password, token):
        value = hashlib.sha256(token.encode('utf-8')).hexdigest()
        if TokenIssued.objects.filter(token=value).count() > 0:
            person = TokenIssued.objects.get(token=value)
            password_change = get_user_model().objects.get(email=person.email)
            person.delete()
            password_change.set_password(password)
            password_change.save()
            return PasswordReset(State='Password Reset was a success')
        else:
            return PasswordReset(State='Something Went Wrong with password reset')

def editClass(object, value):
        if value != None:
            object = value
            return object
        else:
            return object
  
class EditUser(graphene.Mutation):
    user = graphene.Field(User_Info)
    
    class Arguments:
        email = graphene.String(required=True)
        firstName = graphene.String()
        lastName = graphene.String()
        newEmail = graphene.String()
        password = graphene.String()
        picture = graphene.String()
        volunteer = graphene.Boolean()
        isActive = graphene.Boolean()
        isSuperuser = graphene.Boolean()
    
    
    @login_required
    def mutate(self, info, email, newEmail=None, firstName=None, lastName=None, picture=None, volunteer=None, isActive=None, isSuperuser=None, password=None):
        if (get_user_model().objects.get(email=info.context.user.email).is_superuser or get_user_model().objects.get(email=email).email == info.context.user.email):
            user = get_user_model().objects.get(email=email)
            user.email = editClass(user.email, newEmail)
            user.first_name = editClass(user.first_name,firstName)
            user.Last_name = editClass(user.Last_name,lastName)
            user.Picture = editClass(user.Picture,picture)
            if (get_user_model().objects.get(email=info.context.user.email).is_superuser):
                user.Volunteer = editClass(user.Volunteer,volunteer)
                user.is_active = editClass(user.is_active,isActive)
                user.is_superuser = editClass(user.is_superuser,isSuperuser)
            
            if password != None:
                user.set_password(password)
            user.save()
            print('yes')
            return EditUser(user=user)
        
class InviteUser(graphene.Mutation):
    info = graphene.String()
    
    class Arguments:
        email = graphene.String(required=True)
    
    def mutate(self, info, email):
        encoded_jwt = jwt.encode({'Purpose': 'Creating an account', "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=5)}, settings.SECRET_KEY, algorithm="HS256")
        TokenIssued(token=hashlib.sha256(encoded_jwt.encode('utf-8')).hexdigest(), email=email).save()
        return InviteUser(info=encoded_jwt)
    
class PasswordResetEmail(graphene.Mutation):
    info = graphene.String()
    
    class Arguments:
        email = graphene.String(required=True)
    
    def mutate(self, info, email):
        if get_user_model().objects.filter(email=email).count() > 0:
            encoded_jwt = jwt.encode({'Purpose': 'Reset Password', "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)}, settings.SECRET_KEY, algorithm="HS256")
            TokenIssued(token=hashlib.sha256(encoded_jwt.encode('utf-8')).hexdigest(), email=email).save()
            return InviteUser(info=encoded_jwt)
        else:
            return InviteUser(info='Working')

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(User_Info)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

class Query(graphene.ObjectType):
    all_Users = graphene.List(User_Info)
    current_User = graphene.Field(User_Info)
    
    @superuser_required
    def resolve_all_Users(root, info):
        print('yes')
        return get_user_model().objects.all()
    
    @login_required
    def resolve_current_User(root, info):
        return get_user_model().objects.get(email=info.context.user.email)
    
class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    delete_token_cookie = graphql_jwt.relay.DeleteJSONWebTokenCookie.Field()
    create_user = CreateUser.Field()
    edit_user = EditUser.Field()
    invite_User = InviteUser.Field()
    password_request = PasswordResetEmail.Field()
    reset_password = PasswordReset.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)