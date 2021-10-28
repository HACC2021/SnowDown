import graphene
from graphene_django import DjangoObjectType
from .models import Animal_Table
from graphql_jwt.decorators import login_required, superuser_required

class Animal_Info(DjangoObjectType):
    class Meta:
        model = Animal_Table
        fields = ("animal",)
        
class add_Animal(graphene.Mutation):
    new_Animal = graphene.Field(Animal_Info)
    
    class Arguments:
        name = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name):
        animal = Animal_Table(animal=name)
        animal.save()
        
        return add_Animal(new_Animal=animal)
    

class edit_Animal(graphene.Mutation):
    new_Animal = graphene.Field(Animal_Info)
    
    class Arguments:
        name = graphene.String(required=True)
        newName = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name, newName):
        if Animal_Table.objects.filter(animal=name).count() > 0:
            animal = Animal_Table.objects.get(animal=name)
            animal.animal = newName
            animal.save()
            
            return add_Animal(new_Animal=animal)
        else:
            return add_Animal(old_Animal= name + "does not exist")
    

class delete_Animal(graphene.Mutation):
    old_Animal = graphene.String()
    
    class Arguments:
        name = graphene.String(required=True)
        
    @superuser_required
    def mutate(self, info, name):
        if Animal_Table.objects.filter(animal=name).count() > 0:
            animal = Animal_Table.objects.get(animal=name)
            animal.delete()
            
            return delete_Animal(old_Animal= name + " has been deleted")
        else:
            return delete_Animal(old_Animal= name + " does not exist")