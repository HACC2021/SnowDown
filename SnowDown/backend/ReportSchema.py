from graphene_django import DjangoObjectType
import graphene
import datetime
from django.core.files.base import ContentFile
import base64
import math
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
from graphene_file_upload.scalars import Upload
from .models import Incident_Table, SubAnimal_Table, Observer_Type, Sector, SealSize, Sex, TagSide, TagColor, Status, Death, FAST as F, Location, How_ID, Island,\
    Incident_Photos_Table, Group_Incident_Table, Ticket_Type
    
class Master_Report_Info(DjangoObjectType):
    class Meta:
        model = Group_Incident_Table
        fields="__all__"
    animal_images = graphene.List(graphene.String)
    
    def resolve_animal_images(root, info):
        images = [b.photo.url for i in root.incident.all() for b in i.photos.all()]
        return images
        
class Paginated_Report(graphene.ObjectType):
    paginationNum = graphene.Int()
    AmountOfPagination = graphene.Int()
    data = graphene.List(Master_Report_Info)
    
    def resolve_paginationNum(root, info):
        return root['pagination']
    def resolve_AmountOfPagination(root, info):
        return root['amount']
    def resolve_data(root, info):
        start=0+(25*(int(root['pagination'])-1))
        end=25+(25*(int(root['pagination'])-1))
        if len(root['filter'].keys()) == 0:
            num = Group_Incident_Table.objects.all()[start:end]
        else:
            num = Group_Incident_Table.objects.filter(**root['filter']).order_by('dateTime')[start:end]
        return num
        
class query(graphene.ObjectType):
    all_Reports = graphene.List(Master_Report_Info)
    single_Report = graphene.Field(Master_Report_Info, TicketNum = graphene.String(required=True))
    all_FilterReports = graphene.List(Master_Report_Info, StartDate=graphene.String(), EndDate=graphene.String(), Animals=graphene.String(required=True))
    Paginated_Report = graphene.Field(Paginated_Report, pagination=graphene.String(required=True), StartDate=graphene.String(), EndDate=graphene.String(), TicketNumber=graphene.String(), Animal=graphene.String(), SpecificAnimal=graphene.String())
    
    @login_required
    def resolve_all_Reports(root, info):
        data = Group_Incident_Table.objects.all()
        return(data)
    
    @login_required
    def resolve_single_Report(root, info, TicketNum):
        data = Group_Incident_Table.objects.get(Ticket_Number=TicketNum)
        return data
    
    @login_required
    def resolve_all_FilterReports(root, info, Animals, StartDate=None, EndDate=None):
        data_filter = {'dateTime__gte':StartDate, 'dateTime__lte':EndDate, 'animalType__animal__animal': Animals}
        filterData = {k: v for k, v in data_filter.items() if v is not None}
        if 'dateTime__gte' in filterData.keys():
            filterData['dateTime__gte'] = datetime.datetime.strptime(filterData['dateTime__gte'], '%m/%d/%Y').strftime('%Y-%m-%d %H:%M')
        if 'dateTime__lte' in filterData.keys():
            filterData['dateTime__lte'] = datetime.datetime.strptime(filterData['dateTime__lte'], '%m/%d/%Y').strftime('%Y-%m-%d %H:%M')
        print(filterData)
        num = Group_Incident_Table.objects.filter(**filterData)
        return num
        
    @login_required
    def resolve_Paginated_Report(root, info, pagination, StartDate=None, EndDate=None, TicketNumber=None, Animal=None, SpecificAnimal=None):
        data_filter = {'dateTime__gte':StartDate, 'dateTime__lte':EndDate, 'Ticket_Number':TicketNumber,'animalType__animal__animal': Animal, 'animalType__subAnimal':SpecificAnimal}
        filterData = {k: v for k, v in data_filter.items() if v is not None}
        if 'dateTime__gte' in filterData.keys():
            filterData['dateTime__gte'] = datetime.datetime.strptime(filterData['dateTime__gte'], '%m/%d/%Y').strftime('%Y-%m-%d %H:%M')
        if 'dateTime__lte' in filterData.keys():
            filterData['dateTime__lte'] = datetime.datetime.strptime(filterData['dateTime__lte'], '%m/%d/%Y').strftime('%Y-%m-%d %H:%M')
        if len(filterData.keys()) == 0:
            num = Group_Incident_Table.objects.all().count()
        else:
            num = Group_Incident_Table.objects.filter(**filterData).count()
        group = 25
        amount = math.ceil(num/group)
        return {'pagination': int(pagination), 'amountGrouped': group, 'filter':filterData, 'amount':amount}