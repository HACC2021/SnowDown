from graphene_django import DjangoObjectType
from .models import SubAnimal_Table

class SubAnimal_Info(DjangoObjectType):
    class Meta:
        model = SubAnimal_Table
        fields = ("subAnimal", "animal",)