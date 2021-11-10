from graphene_django import DjangoObjectType
import graphene
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
from .models import SubAnimal_Table, Animal_Table

class SubAnimal_Info(DjangoObjectType):
    class Meta:
        model = SubAnimal_Table
        fields = ("subAnimal", "animal", "acronym",)
        
class query(graphene.ObjectType):
    all_SubAnimals = graphene.List(SubAnimal_Info)
    
    def resolve_all_SubAnimals(root, info):
        return SubAnimal_Table.objects.all()
        
class add_SubAnimal(graphene.Mutation):
    new_Animal = graphene.Field(SubAnimal_Info)
    
    class Arguments:
        name = graphene.String(required=True)
        animal = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name, animal):
        parentAnimal = Animal_Table.objects.get(animal=animal)
        animal = SubAnimal_Table(subAnimal=name , animal=parentAnimal)
        animal.save()
        
        return add_SubAnimal(new_Animal=animal)
    

class edit_SubAnimal(graphene.Mutation):
    new_Animal = graphene.Field(SubAnimal_Info)
    
    class Arguments:
        name = graphene.String(required=True)
        newName = graphene.String(required=True)
        animal = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name, newName, animal):
        if SubAnimal_Table.objects.filter(subAnimal=name).count() > 0:
            parentAnimal = Animal_Table.objects.get(animal=animal)
            animal = SubAnimal_Table.objects.get(subAnimal=name)
            animal.subAnimal = newName
            animal.animal = parentAnimal
            animal.save()
            
            return edit_SubAnimal(new_Animal=animal)
        else:
            return GraphQLError(name + "does not exist")
    

class delete_SubAnimal(graphene.Mutation):
    old_Animal = graphene.String()
    
    class Arguments:
        name = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name):
        if SubAnimal_Table.objects.filter(subAnimal=name).count() > 0:
            animal = SubAnimal_Table.objects.get(subAnimal=name)
            animal.delete()
            
            return delete_SubAnimal(old_Animal= name + " has been deleted")
        else:
            return GraphQLError(name + "does not exist")