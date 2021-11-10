from graphene_django import DjangoObjectType
import graphene
from graphql_jwt.decorators import login_required

from .models import Ticket_Type, Observer_Type, Sector, SealSize, Sex, TagSide, TagColor, Status,\
    Death, FAST, Location, How_ID, Island

class Ticket_Info(DjangoObjectType):
    class Meta:
        model = Ticket_Type
        fields="__all__"
        
class Observer_Info(DjangoObjectType):
    class Meta:
        model = Observer_Type
        fields="__all__"
        
class Sector_Info(DjangoObjectType):
    class Meta:
        model = Sector
        fields="__all__"
        
class SealSize_Info(DjangoObjectType):
    class Meta:
        model = SealSize
        fields="__all__"
        
class Sex_Info(DjangoObjectType):
    class Meta:
        model = Sex
        fields="__all__"
        
class TagSide_Info(DjangoObjectType):
    class Meta:
        model = TagSide
        fields="__all__"
        
class TagColor_Info(DjangoObjectType):
    class Meta:
        model = TagColor
        fields="__all__"
        
class Death_Info(DjangoObjectType):
    class Meta:
        model = Death
        fields="__all__"
        
class FAST_Info(DjangoObjectType):
    class Meta:
        model = FAST
        fields="__all__"
        
class Location_Info(DjangoObjectType):
    class Meta:
        model = Location
        fields="__all__"
        
class How_ID_Info(DjangoObjectType):
    class Meta:
        model = How_ID
        fields="__all__"
        
class Island_Info(DjangoObjectType):
    class Meta:
        model = Island
        fields="__all__"
        
class Status_Info(DjangoObjectType):
    class Meta:
        model = Status
        fields="__all__"


class query(graphene.ObjectType):
    all_Tickets = graphene.List(Ticket_Info)
    all_Observer = graphene.List(Observer_Info)
    all_Sectors = graphene.List(Sector_Info)
    all_SealSize = graphene.List(SealSize_Info)
    all_Sex = graphene.List(Sex_Info)
    all_TagSide = graphene.List(TagSide_Info)
    all_TagColor = graphene.List(TagColor_Info)
    all_Death = graphene.List(Death_Info)
    all_FAST = graphene.List(FAST_Info)
    all_Location = graphene.List(Location_Info)
    all_How_ID = graphene.List(How_ID_Info)
    all_Island = graphene.List(Island_Info)
    all_Status = graphene.List(Status_Info)
    
    #@login_required
    def resolve_all_Tickets(root, info):
        return Ticket_Type.objects.all()
    
    #@login_required
    def resolve_all_Observer(root, info):
        return Observer_Type.objects.all()
    
    def resolve_all_Sectors(root, info):
        return Sector.objects.all()
    
    def resolve_all_SealSize(root, info):
        return SealSize.objects.all()
    
    def resolve_all_Sex(root, info):
        return Sex.objects.all()
    
    def resolve_all_TagSide(root, info):
        return TagSide.objects.all()
    
    def resolve_all_TagColor(root, info):
        return TagColor.objects.all()
    
    def resolve_all_Death(root, info):
        return Death.objects.all()
    
    def resolve_all_FAST(root, info):
        return FAST.objects.all()
    
    def resolve_all_Location(root, info):
        return Location.objects.all()
    
    def resolve_all_How_ID(root, info):
        return How_ID.objects.all()
    
    def resolve_all_Island(root, info):
        return Island.objects.all()
    
    def resolve_all_Status(root, info):
        print('yes')
        return Status.objects.all()

