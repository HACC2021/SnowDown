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
        
class Create_Incident(graphene.Mutation):
    report = graphene.String()
    
    class Arguments:
        lat = graphene.Float(required=True)
        lng = graphene.Float(required=True)
        location = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone = graphene.String(required=True)
        email = graphene.String(required=True)
        animal = graphene.String(required=True)
        description = graphene.String(required=True)
        people = graphene.Int(required=True)
        characteristics = graphene.List(graphene.String, required=True)
        photos = graphene.List(Upload, required=True)
        
    def mutate(self, info, lat, lng, location, first_name, last_name, phone, email, animal, description, people, characteristics, photos):
        animal = SubAnimal_Table.objects.get(subAnimal=animal)
        incident = Incident_Table(dateTime=datetime.now(), 
                                  lat=lat, 
                                  lng=lng, 
                                  location=location,
                                  firstName=first_name,
                                  lastName=last_name,
                                  phone=phone,
                                  email=email,
                                  animal=animal,
                                  description=description,
                                  people=people)
        incident.save()
        for i in characteristics:
            try:
                tag = Animal_Characteristics_Table(characteristicsTag=i.lower())
                tag.save()
                taged = Animal_Characteristics_Table.objects.get(characteristicsTag=i.lower())
            except:
                tag = Animal_Characteristics_Table.objects.get(characteristicsTag=i.lower())
                incident.characteristics.add(tag.pk)
        """for i in photos:
            try:
                tag = Incident_Photos_Table(photo=i)
                tag.save()
                incident.characteristics.add(tag)
            except:
                tag = Incident_Photos_Table.objects.get(photo=i)
                incident.characteristics.add(tag)"""
        return Create_Incident(report='Complete')
        