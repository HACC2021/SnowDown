from graphene_django import DjangoObjectType
import graphene
import datetime
from django.core.files.base import ContentFile
import base64
import pytz
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, superuser_required
from graphene_file_upload.scalars import Upload
from .models import Incident_Table, SubAnimal_Table, Observer_Type, Sector, SealSize, Sex, TagSide, TagColor, Status, Death, FAST as F, Location, How_ID, Island,\
    Incident_Photos_Table, Group_Incident_Table, Ticket_Type

class Incident_Info(DjangoObjectType):
    class Meta:
        model=Incident_Table
        fields="__all__"
        
class add_Incident(graphene.Mutation):
    succcesses = graphene.String()
    
    class Arguments:
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        phoneNumber = graphene.String(required=True)
        email = graphene.String(required=True)
        location = graphene.String(required=True)
        lat = graphene.Float(required=True)
        lng = graphene.Float(required=True)
        locationDescription = graphene.String(required=True)
        sector = graphene.String(required=True)
        animalType = graphene.String(required=True)
        animalPresent = graphene.Boolean(required=True)
        sealSize = graphene.String()
        sex = graphene.String()
        landOrWater = graphene.Boolean()
        howIdentified = graphene.String()
        tagSide = graphene.String()
        tagColor = graphene.String()
        tagNumber = graphene.String()
        bleachNum = graphene.String()
        IDPerm = graphene.String()
        IDNotes = graphene.String()
        molting = graphene.Boolean()
        sealLogging = graphene.Boolean()
        animalWithBaby = graphene.Boolean()
        SRASetUp = graphene.Boolean()
        sealDeparted = graphene.Boolean()
        SRAPerson = graphene.String()
        dateDeparted = graphene.String()
        timeDeparted = graphene.String()
        turtleSize = graphene.String()
        FAST = graphene.String()
        status = graphene.String()
        issue = graphene.String()
        delivered = graphene.Boolean()
        deliverdLocation = graphene.String()
        OperatorOutReach = graphene.Boolean()
        onIsland = graphene.String()
        responderName = graphene.String()
        amountOfResponders = graphene.String()
        timeArrived = graphene.String()
        timeLeft = graphene.String()
        description = graphene.String(required=True)
        images = graphene.List(graphene.String, required=True)
        hotLineOperatorInit = graphene.String()
        observer_type = graphene.String()
    
    @login_required
    def mutate(self, info, firstName=None, lastName=None, phoneNumber=None, email=None, location=None, lat=None, lng=None, locationDescription=None, sector=None, animalType=None, animalPresent=None,
               sealSize=None, sex=None, landOrWater=None, howIdentified=None, tagSide=None, tagColor=None, tagNumber=None, bleachNum=None, IDPerm=None, IDNotes=None, molting=None, sealLogging=None,
               animalWithBaby=None, SRASetUp=None, sealDeparted=None, SRAPerson=None, dateDeparted=None, timeDeparted=None, turtleSize=None, FAST=None, status=None, issue=None, delivered=None,
               deliverdLocation=None, OperatorOutReach=None, onIsland=None, responderName=None, amountOfResponders=None, timeArrived=None, timeLeft=None, description=None, images=None, hotLineOperatorInit="N/A", observer_type='Public'):
        try:
            subAnimal = SubAnimal_Table.objects.get(subAnimal=animalType)
            timedate = datetime.datetime.now(tz=pytz.timezone('US/Hawaii'))
            observer_type = Observer_Type.objects.get(observer_type=observer_type)
            sector = Sector.objects.get(observer_type=sector)
            ticket=Ticket_Type.objects.get(ticket_type='Incident')
            date = timedate.date()
            time = timedate.time()
            if subAnimal.animal.animal == 'Seal':
                verified_By=''
                if len(IDPerm) != 0:
                    verified_By=firstName
                sealSize = SealSize.objects.get(options=sealSize)
                sex = Sex.objects.get(options=sex)
                how_ID = How_ID.objects.get(options=howIdentified)
                try:
                    side = TagSide.objects.get(options=tagSide)
                    color = TagColor.objects.get(options=tagColor)
                except:
                    side=None
                    color=None
                newIncident = Incident_Table(dateTime=timedate,
                                            Date=date.strftime("%m/%d/%Y"),
                                            Time=time.strftime("%H:%M"),
                                            Hotline_Operator_Initials=hotLineOperatorInit,
                                            Ticket_Type=ticket,
                                            firstName=firstName,
                                            lastName=lastName,
                                            phone=phoneNumber,
                                            email=email,
                                            Observer_Initials=firstName[0]+lastName[0],
                                            Observer_Type=observer_type,
                                            Sector=sector,
                                            location=location,
                                            lat=lat,
                                            lng=lng,
                                            locationDetails=locationDescription,
                                            Animal_Present=bool(animalPresent),
                                            SealSize=sealSize,
                                            sex=sex,
                                            beach_Position=bool(landOrWater),
                                            How_ID=how_ID,
                                            BleachNumber=bleachNum,
                                            Tag_Number=tagNumber,
                                            Tag_Side=side,
                                            Tag_Color=color,
                                            ID_Perm=IDPerm,
                                            Molt=bool(molting),
                                            ID_Description=IDNotes,
                                            ID_Verified_by=verified_By,
                                            SealLogging=bool(sealLogging),
                                            MomPup=bool(animalWithBaby),
                                            SRA_Set_Up=bool(SRASetUp),
                                            SRA_Set_by = SRAPerson,
                                            Volunteers_Engaged=amountOfResponders,
                                            Seal_Depart=bool(sealDeparted),
                                            Seal_Depart_Date=dateDeparted,
                                            Seal_Depart_Time=timeDeparted,
                                            animalType=subAnimal,
                                            Responder=responderName,
                                            Responder_Arrived=timeArrived,
                                            Responder_Left=timeLeft,
                                            Outreach_Provided=OperatorOutReach,
                                            description=description)
            elif subAnimal.animal.animal == 'Sea Birds':
                dellocation = None
                if deliverdLocation == "":
                    try:
                        dellocation = Location.objects.get(options=deliverdLocation)
                    except:
                        dellocation = None
                newIncident = Incident_Table(dateTime=timedate,
                                            Date=date.strftime("%m/%d/%Y"),
                                            Time=time.strftime("%H:%M"),
                                            Hotline_Operator_Initials=hotLineOperatorInit,
                                            Ticket_Type=ticket,
                                            firstName=firstName,
                                            lastName=lastName,
                                            phone=phoneNumber,
                                            email=email,
                                            Observer_Initials=firstName[0]+lastName[0],
                                            Observer_Type=observer_type,
                                            Sector=sector,
                                            location=location,
                                            lat=lat,
                                            lng=lng,
                                            locationDetails=locationDescription,
                                            Animal_Present=bool(animalPresent),
                                            Volunteers_Engaged=amountOfResponders,
                                            animalType=subAnimal,
                                            Responder=responderName,
                                            Responder_Arrived=timeArrived,
                                            Responder_Left=timeLeft,
                                            Outreach_Provided=OperatorOutReach,
                                            Delivered=bool(delivered),
                                            Where_To=dellocation,
                                            description=description)
            else:
                status = Status.objects.get(options=status)
                try:
                    FAST = F.objects.get(options=FAST)
                except:
                    FAST = None
                island = Island.objects.get(island=onIsland)
                injury = Death.objects.get(options = issue)
                newIncident = Incident_Table(dateTime=timedate,
                                            Date=date.strftime("%m/%d/%Y"),
                                            Time=time.strftime("%H:%M"),
                                            Ticket_Number=str(subAnimal.animal.acronym) + date.strftime("%m%d%Y") + time.strftime("%H%M"),
                                            Hotline_Operator_Initials=hotLineOperatorInit,
                                            Ticket_Type=ticket,
                                            firstName=firstName,
                                            lastName=lastName,
                                            phone=phoneNumber,
                                            email=email,
                                            Observer_Initials=firstName[0]+lastName[0],
                                            Observer_Type=observer_type,
                                            Sector=sector,
                                            location=location,
                                            lat=lat,
                                            lng=lng,
                                            locationDetails=locationDescription,
                                            Animal_Present=bool(animalPresent),
                                            Volunteers_Engaged=amountOfResponders,
                                            animalType=subAnimal,
                                            size=turtleSize,
                                            status=status,
                                            CauseOfDeath=injury,
                                            onIsland=island,
                                            Responder=responderName,
                                            Responder_Arrived=timeArrived,
                                            Responder_Left=timeLeft,
                                            Outreach_Provided=OperatorOutReach,
                                            FAST=FAST,
                                            description=description)
            newIncident.save()
            for i in images:
                time = datetime.datetime.now(tz=datetime.timezone.utc)
                format, imgstr = i.split(';base64,')
                ext = format.split('/')[-1] 
                img = ContentFile(base64.b64decode(imgstr), name=str(time) + '.' + ext)
                pic = Incident_Photos_Table(photo=img)
                pic.save()
                newIncident.photos.add(pic)
            chain = Group_Incident_Table.objects.filter(Top__gte=float(lat), Bottom__lte=float(lat), Right__gte=float(lng), Left__lte=float(lng), Date=date.strftime("%m/%d/%Y"), animalType=subAnimal)
            chainNumber = chain.count()
            if chainNumber > 0:
                print('yes')
                num = ''
                for ind, value in enumerate(chain):
                    if ind == 0:
                        num = value.Ticket_Number
                    else:
                        pass
                print('yes')
                combine = Group_Incident_Table.objects.get(Ticket_Number=num)
                combine.incident.add(newIncident)
                values = [f.name for f in Group_Incident_Table._meta.get_fields() if (getattr(combine, str(f.name)) == None or getattr(combine, str(f.name)) == '')and f.name!='incident']
                for i in values:
                    setattr(combine, i, getattr(newIncident,i))
            else:
                if subAnimal.animal.animal == 'Seal':
                    verified_By=''
                    if len(IDPerm) != 0:
                        verified_By=firstName
                    sealSize = SealSize.objects.get(options=sealSize)
                    sex = Sex.objects.get(options=sex)
                    how_ID = How_ID.objects.get(options=howIdentified)
                    try:
                        side = TagSide.objects.get(options=tagSide)
                        color = TagColor.objects.get(options=tagColor)
                    except:
                        side=None
                        color=None
                    group_new = Group_Incident_Table(dateTime=timedate,
                                                Date=date.strftime("%m/%d/%Y"),
                                                Time=time.strftime("%H:%M"),
                                                Top=lat+0.0005,
                                                Bottom=lat-0.0005,
                                                Left = lng-0.0005,
                                                Right=lng+0.0005,
                                                Ticket_Number=str(subAnimal.animal.acronym) + date.strftime("%m%d%Y") + time.strftime("%H%M"),
                                                Hotline_Operator_Initials=hotLineOperatorInit,
                                                Ticket_Type=ticket,
                                                firstName=firstName,
                                                lastName=lastName,
                                                phone=phoneNumber,
                                                email=email,
                                                Observer_Initials=firstName[0]+lastName[0],
                                                Observer_Type=observer_type,
                                                Sector=sector,
                                                location=location,
                                                lat=lat,
                                                lng=lng,
                                                locationDetails=locationDescription,
                                                Animal_Present=bool(animalPresent),
                                                SealSize=sealSize,
                                                sex=sex,
                                                beach_Position=bool(landOrWater),
                                                How_ID=how_ID,
                                                BleachNumber=bleachNum,
                                                Tag_Number=tagNumber,
                                                Tag_Side=side,
                                                Tag_Color=color,
                                                ID_Perm=IDPerm,
                                                Molt=bool(molting),
                                                ID_Description=IDNotes,
                                                ID_Verified_by=verified_By,
                                                SealLogging=bool(sealLogging),
                                                MomPup=bool(animalWithBaby),
                                                SRA_Set_Up=bool(SRASetUp),
                                                SRA_Set_by = SRAPerson,
                                                Volunteers_Engaged=amountOfResponders,
                                                Seal_Depart=bool(sealDeparted),
                                                Seal_Depart_Date=dateDeparted,
                                                Seal_Depart_Time=timeDeparted,
                                                animalType=subAnimal,
                                                Responder=responderName,
                                                Responder_Arrived=timeArrived,
                                                Responder_Left=timeLeft,
                                                Outreach_Provided=OperatorOutReach,
                                                description=description)
                elif subAnimal.animal.animal == 'Sea Birds':
                    group_new = Group_Incident_Table(dateTime=timedate,
                                                Date=date.strftime("%m/%d/%Y"),
                                                Time=time.strftime("%H:%M"),
                                                Top=lat+0.0005,
                                                Bottom=lat-0.0005,
                                                Left = lng-0.0005,
                                                Right=lng+0.0005,
                                                Ticket_Number=str(subAnimal.animal.acronym) + date.strftime("%m%d%Y") + time.strftime("%H%M"),
                                                Hotline_Operator_Initials=hotLineOperatorInit,
                                                Ticket_Type=ticket,
                                                firstName=firstName,
                                                lastName=lastName,
                                                phone=phoneNumber,
                                                email=email,
                                                Observer_Initials=firstName[0]+lastName[0],
                                                Observer_Type=observer_type,
                                                Sector=sector,
                                                location=location,
                                                lat=lat,
                                                lng=lng,
                                                locationDetails=locationDescription,
                                                Animal_Present=bool(animalPresent),
                                                Volunteers_Engaged=amountOfResponders,
                                                animalType=subAnimal,
                                                Responder=responderName,
                                                Responder_Arrived=timeArrived,
                                                Responder_Left=timeLeft,
                                                Outreach_Provided=OperatorOutReach,
                                                Delivered=bool(delivered),
                                                Where_To=dellocation,
                                                description=description)
                else:
                    status = Status.objects.get(options=status)
                    try:
                        FAST = F.objects.get(options=FAST)
                    except:
                        FAST = None
                    island = Island.objects.get(island=onIsland)
                    injury = Death.objects.get(options = issue)
                    group_new = Group_Incident_Table(dateTime=timedate,
                                                Date=date.strftime("%m/%d/%Y"),
                                                Top=lat+0.0005,
                                                Bottom=lat-0.0005,
                                                Left = lng-0.0005,
                                                Right=lng+0.0005,
                                                Time=time.strftime("%H:%M"),
                                                Ticket_Number=str(subAnimal.animal.acronym) + date.strftime("%m%d%Y") + time.strftime("%H%M"),
                                                Hotline_Operator_Initials=hotLineOperatorInit,
                                                Ticket_Type=ticket,
                                                firstName=firstName,
                                                lastName=lastName,
                                                phone=phoneNumber,
                                                email=email,
                                                Observer_Initials=firstName[0]+lastName[0],
                                                Observer_Type=observer_type,
                                                Sector=sector,
                                                location=location,
                                                lat=lat,
                                                lng=lng,
                                                locationDetails=locationDescription,
                                                Animal_Present=bool(animalPresent),
                                                Volunteers_Engaged=amountOfResponders,
                                                animalType=subAnimal,
                                                size=turtleSize,
                                                status=status,
                                                CauseOfDeath=injury,
                                                onIsland=island,
                                                Responder=responderName,
                                                Responder_Arrived=timeArrived,
                                                Responder_Left=timeLeft,
                                                Outreach_Provided=OperatorOutReach,
                                                FAST=FAST,
                                                description=description)
                group_new.save()
                group_new.incident.add(newIncident)
                    

                return add_Incident(succcesses='Success')
        except:
            raise GraphQLError('There seems to be an issue')