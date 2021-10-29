from graphene_django import DjangoObjectType
import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
from .models import Animal_Characteristics_Table
from django.db.models import Q
from operator import or_

class AnimalCharacteriscsSchema_Info(DjangoObjectType):
    class Meta:
        model = Animal_Characteristics_Table
        fields = ('characteristicsTag',)
        
class query(graphene.ObjectType):
    AnimalCharacteristics = graphene.List(AnimalCharacteriscsSchema_Info, tags=graphene.List(graphene.String, required=True))
    AnimalCharacteristicsSearch = graphene.List(AnimalCharacteriscsSchema_Info, tag=graphene.String(required=True))
    
    def resolve_AnimalCharacteristics(root, info, tags):
        return Animal_Characteristics_Table.objects.filter(characteristicsTag__in=tags)
    def resolve_AnimalCharacteristicsSearch(root, info, tag):
        return Animal_Characteristics_Table.objects.filter(characteristicsTag__istartswith=tag)
    
class Add_Characteristics(graphene.Mutation):
    value = graphene.String()
    
    class Arguments:
        tags = graphene.List(graphene.String, required=True)

    def mutate(self, info, tags):
        counter= 0
        for i in tags:
            try:
                tag = Animal_Characteristics_Table(characteristicsTag=i.lower())
                tag.save()
                counter += 1
            except:
                pass
        return Add_Characteristics(value = str(counter) + ' tags have been added')
        
        