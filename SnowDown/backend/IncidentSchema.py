from graphene_django import DjangoObjectType
import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
from graphene_file_upload.scalars import Upload
from .models import Incident_Table, Animal_Characteristics_Table, SubAnimal_Table, Incident_Photos_Table
from datetime import datetime


class Incident_Info(DjangoObjectType):
    class Meta:
        model=Incident_Table
        fields="__all__"
        
