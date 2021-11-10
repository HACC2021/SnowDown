import graphene
from graphene_django import DjangoObjectType
import graphql_jwt
from django.conf import settings
from . import Userschemas, Animalschemas, SubAnimalschemas, IncidentSchema, FormSchema, ReportSchema
from django.contrib.auth import get_user_model

from graphql import GraphQLError
from graphql_jwt.utils import get_payload
from .models import Incident_Photos_Table, Incident_Table,\
    Group_Incident_Table, TokenIssued
from graphql_jwt.decorators import login_required, superuser_required


class Query(Userschemas.query, SubAnimalschemas.query, Animalschemas.query, FormSchema.query, ReportSchema.query, graphene.ObjectType):
    pass
    
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
    add_SubAnimal = SubAnimalschemas.add_SubAnimal.Field()
    edit_SubAnimal = SubAnimalschemas.edit_SubAnimal.Field()
    delete_SubAnimal = SubAnimalschemas.delete_SubAnimal.Field()
    add_Incident = IncidentSchema.add_Incident.Field()
    
    
schema = graphene.Schema(query=Query, mutation=Mutation)