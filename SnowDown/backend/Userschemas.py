from django.contrib.auth import get_user_model
import jwt
import graphene
from graphene_django import DjangoObjectType
import hashlib
from .models import TokenIssued
from django.conf import settings
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
import datetime
import graphql_jwt

# User Schemas
# The classes underneath hold the ability to view users, update users, creat users,
# update users, Send password reset emails, reset passwords, sign user in,
# reverify tokens, display current user logged in, and revoke tokens fore people signed in

# This class states what fields are allowed to be queried of the user model
class User_Info(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = ("id", "first_name", "Last_name", 'email', "Volunteer", "Picture", "is_active", "is_superuser")
        
class query(graphene.ObjectType):
    all_Users = graphene.List(User_Info)
    certain_Users = graphene.Field(User_Info, email=graphene.String(required=True))
    current_User = graphene.Field(User_Info)
    
    @superuser_required
    def resolve_all_Users(root, info):
        print('yes')
        return get_user_model().objects.all()
    
    @superuser_required
    def resolve_certain_Users(root, info, email):
        return get_user_model().objects.get(email=email)
    
    @login_required
    def resolve_current_User(root, info):
        return get_user_model().objects.get(email=info.context.user.email)
        
# This class Creats Users. An email has to be sent out with a token
# Once a token is used it no longer works due to it getting revoked from
# the token database. It then checks if the token has expired if so then it
# will send out an error
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
        
# This class resets passwords. It takes the token given
# by an email to see if the token has been used by looking into
# the database. If it has been used or expired then it will send
class PasswordReset(graphene.Mutation):
    State = graphene.String()
    
    class Arguments:
        password = graphene.String(required=True)
        token = graphene.String(required=True)
        
    def mutate(self, info, password, token):
        value = hashlib.sha256(token.encode('utf-8')).hexdigest()
        if TokenIssued.objects.filter(token=value).count() > 0:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            if data['Purpose'] == 'Reset Password':
                person = TokenIssued.objects.get(token=value)
                password_change = get_user_model().objects.get(email=person.email)
                person.delete()
                password_change.set_password(password)
                password_change.save()
                return PasswordReset(State='Password Reset was a success')
        else:
            raise GraphQLError('Something Went Wrong with password reset')

# Used to make sure that the new value is not empty
# if it is then the value assigned is its current value
def editClass(object, value):
        if value != None:
            object = value
            return object
        else:
            return object

# Edit users allows admins/Super users to edit an account.
# This also allowsthe current user to edit there account.
# Uses the editClass function to see if the values are not None.
# You may freeze an account which acts like deleting an account, 
# but we get to keep all the data connected to that account
# !Edit the isActive column to delete a user
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
        
# Invite users sends out an email with a token that is active for up to 5 hours.
# If token is not used within the 5 hours it will expire rendering the token
# useless. Requires an input of an email. User must be admin/super user to complete this action
class InviteUser(graphene.Mutation):
    info = graphene.String()
    
    class Arguments:
        email = graphene.String(required=True)
    
    @superuser_required
    def mutate(self, info, email):
        encoded_jwt = jwt.encode({'Purpose': 'Creating an account', "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=5)}, settings.SECRET_KEY, algorithm="HS256")
        TokenIssued(token=hashlib.sha256(encoded_jwt.encode('utf-8')).hexdigest(), email=email).save()
        return InviteUser(info=encoded_jwt)
    
# Creats a token that will be used to reset passwords
# This tokens then are sent out by email for the person
# Tokens last up to an hour
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
            return InviteUser(info='If this account exists we will be sending out an email')

class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(User_Info)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)
    