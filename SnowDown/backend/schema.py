import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
from django.conf import settings
from . import Userschemas
from . import Animalschemas
from . import SubAnimalschemas
from django.contrib.auth import get_user_model

from graphql import GraphQLError
from graphql_jwt.utils import get_payload
from .models import Animal_Table, SubAnimal_Table, Animal_Characteristics_Table, Incident_Photos_Table, Incident_Table, Incident_Before_Photos_Table,\
    Incident_After_Photos_Table, Group_Incident_Table, TokenIssued
from graphql_jwt.decorators import login_required, superuser_required


class Query(graphene.ObjectType):
    all_Users = graphene.List(Userschemas.User_Info)
    current_User = graphene.Field(Userschemas.User_Info)
    all_Animals = graphene.List(Animalschemas.Animal_Info)
    single_Animal = graphene.Field(Animalschemas.Animal_Info)
    all_SubAnimals = graphene.List(SubAnimalschemas.SubAnimal_Info)
    
    @superuser_required
    def resolve_all_Users(root, info):
        print('yes')
        return get_user_model().objects.all()
    
    @login_required
    def resolve_current_User(root, info):
        return get_user_model().objects.get(email=info.context.user.email)
    
    def resolve_all_Animals(root, info):
        return Animal_Table.objects.all()
    def resolve_all_SubAnimals(root, info):
        return SubAnimal_Table.objects.all()
    
    
class Mutation(graphene.ObjectType):
    token_auth = Userschemas.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    delete_token_cookie = graphql_jwt.relay.DeleteJSONWebTokenCookie.Field()
    create_user = Userschemas.CreateUser.Field()
    edit_user = Userschemas.EditUser.Field()
    invite_User = Userschemas.InviteUser.Field()
    password_request = Userschemas.PasswordResetEmail.Field()
    reset_password = Userschemas.PasswordReset.Field()
    add_Animals = Animalschemas.add_Animal.Field()
    delete_Animals = Animalschemas.delete_Animal.Field()
    edit_Animals = Animalschemas.edit_Animal.Field()
    
schema = graphene.Schema(query=Query, mutation=Mutation)