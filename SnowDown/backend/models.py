from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, Last_name, phone, password=None, **extra_fields):
        #Creates and saves a new user
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), first_name=first_name, Last_name=Last_name,
                          phone=phone, **extra_fields)
        user.set_password(password)
        user.is_active = False
        user.save(using=self._db)

        return user

    def create_Volunteer(self, email, first_name, Last_name, phone, password):
        user = self.create_user(email, first_name, Last_name, phone, password)
        user.is_staff = True
        user.is_superuser = False
        user.is_active = True
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, Last_name, Picture, phone, password):
        user = self.create_user(email, first_name, Last_name, phone, password)
        user.is_staff = True
        user.is_superuser = True
        user.agent = True
        user.is_active = True
        user.Picture = Picture
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    # Custom user model that supports using email instead of username
    email = models.EmailField(max_length=225, unique=True)
    phone = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    Volunteer = models.BooleanField(default=True)
    Picture = models.ImageField(upload_to='User Profile Pic/', default='User Profile Pic/default.png', )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['first_name', 'Last_name', 'Picture', 'phone']

    USERNAME_FIELD = 'email'
    
class TokenIssued(models.Model):
    token=models.TextField()
    email=models.EmailField(max_length=225)
    
    def __str__(self):
        return self.token
# Animal type
class Animal_Table(models.Model):
    animal = models.CharField(max_length=400, unique=True)
    acronym=models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.animal
    
# Animal Sub category
class SubAnimal_Table(models.Model):
    subAnimal = models.CharField(max_length=400, unique=True)
    acronym=models.CharField(max_length=200, blank=True)
    animal = models.ForeignKey(Animal_Table, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.animal.__str__() + ', ' + self.subAnimal.__str__()

# Animal Characteristics
class Incident_Photos_Table(models.Model):
    photo = models.ImageField(upload_to='Report_Images/')
    
class Ticket_Type(models.Model):
    ticket_type = models.CharField(max_length=100)
    acronym=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.ticket_type.__str__()
    
class Observer_Type(models.Model):
    observer_type = models.CharField(max_length=20)
    acronym=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.observer_type.__str__()
    
class Sector(models.Model):
    observer_type = models.CharField(max_length=20)
    def __str__(self):
        return self.observer_type.__str__()
    
class SealSize(models.Model):
    options = models.CharField(max_length=30)
    acronym=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.options.__str__()
    
class Sex(models.Model):
    options = models.CharField(max_length=30)
    def __str__(self):
        return self.options.__str__()
    
class TagSide(models.Model):
    options = models.CharField(max_length=30)
    def __str__(self):
        return self.options.__str__()
    
class TagColor(models.Model):
    options = models.CharField(max_length=10)
    def __str__(self):
        return self.options.__str__()
    
class Status(models.Model):
    options = models.CharField(max_length=10)
    def __str__(self):
        return self.options.__str__()
    
class Death(models.Model):
    options = models.CharField(max_length=30)
    def __str__(self):
        return self.options.__str__()
    
class FAST(models.Model):
    options = models.CharField(max_length=10)
    def __str__(self):
        return self.options.__str__()
    
class Location(models.Model):
    options = models.CharField(max_length=30)
    def __str__(self):
        return self.options.__str__()
    
class How_ID(models.Model):
    options = models.CharField(max_length=30)
    acronym=models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.options.__str__()

class Island(models.Model):
    island = models.CharField(max_length=30)
    def __str__(self):
        return self.island.__str__()
    

# Holds the Incidents people have reported
class Incident_Table(models.Model):
    dateTime = models.DateTimeField()
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Ticket_Number = models.CharField(max_length=15)
    Hotline_Operator_Initials = models.CharField(max_length=4, blank=True)
    Ticket_Type = models.ForeignKey(Ticket_Type, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    Observer_Initials = models.CharField(max_length=4)
    Observer_Type = models.ForeignKey(Observer_Type, on_delete=models.CASCADE)
    Sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    lat = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    lng = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    locationDetails = models.TextField(blank=True, null=True)
    Animal_Present = models.BooleanField(default=False, blank=True, null=True)
    SealSize = models.ForeignKey(SealSize, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, blank=True, null=True)
    beach_Position = models.BooleanField(blank=True, null=True)
    How_ID = models.ForeignKey(How_ID, on_delete=models.CASCADE, blank=True, null=True)
    BleachNumber = models.CharField(max_length=10, blank=True, null=True)
    Tag_Number = models.CharField(max_length=10, blank=True, null=True)
    Tag_Side = models.ForeignKey(TagSide, blank=True, null=True, on_delete=models.CASCADE)
    Tag_Color = models.ForeignKey(TagColor, blank=True, null=True, on_delete=models.CASCADE)
    ID_Perm = models.CharField(max_length=10, blank=True, null=True)
    Molt = models.BooleanField(blank=True, null=True)
    ID_Description = models.TextField(blank=True, null=True)
    ID_Verified_by = models.CharField(max_length=100)
    SealLogging = models.BooleanField(blank=True, null=True)
    MomPup = models.BooleanField(blank=True, null=True)
    SRA_Set_Up = models.BooleanField(blank=True, null=True)
    SRA_Set_by = models.CharField(max_length=100, blank=True, null=True)
    Volunteers_Engaged = models.IntegerField(blank=True, null=True)
    Seal_Depart = models.BooleanField(blank=True, null=True)
    Seal_Depart_Date = models.DateField(blank=True, null=True)
    Seal_Depart_Time = models.TimeField(blank=True, null=True)
    description = models.TextField()
    photos = models.ManyToManyField(Incident_Photos_Table)
    animalType = models.ForeignKey(SubAnimal_Table, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, blank=True, null=True)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    CauseOfDeath = models.ForeignKey(Death, blank=True, null=True, on_delete=models.CASCADE)
    Responder = models.CharField(max_length=100, blank=True, null=True)
    Responder_Arrived = models.TimeField(blank=True, null=True)
    Responder_Left = models.TimeField(blank=True, null=True)
    Outreach_Provided = models.BooleanField()
    FAST = models.ForeignKey(FAST, blank=True, null=True, on_delete=models.CASCADE)
    Delivered = models.BooleanField(blank=True, null=True)
    Where_To = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    onIsland = models.ForeignKey(Island, blank=True, null=True, on_delete=models.CASCADE)
    
class Group_Incident_Table(models.Model):
    incident = models.ManyToManyField(Incident_Table)
    Top=models.DecimalField(max_digits=19, decimal_places=15)
    Bottom=models.DecimalField(max_digits=19, decimal_places=15)
    Left=models.DecimalField(max_digits=19, decimal_places=15)
    Right=models.DecimalField(max_digits=19, decimal_places=15)
    dateTime = models.DateTimeField()
    Date = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    Ticket_Number = models.CharField(max_length=15)
    Hotline_Operator_Initials = models.CharField(max_length=4, blank=True, null=True)
    Ticket_Type = models.ForeignKey(Ticket_Type, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    Observer_Initials = models.CharField(max_length=4)
    Observer_Type = models.ForeignKey(Observer_Type, on_delete=models.CASCADE)
    Sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    location = models.CharField(max_length=500)
    lat = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    lng = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    locationDetails = models.TextField(blank=True, null=True)
    Animal_Present = models.BooleanField(default=False, blank=True, null=True)
    SealSize = models.ForeignKey(SealSize, on_delete=models.CASCADE, blank=True, null=True)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE, blank=True, null=True)
    beach_Position = models.BooleanField(blank=True, null=True)
    How_ID = models.ForeignKey(How_ID, on_delete=models.CASCADE, blank=True, null=True)
    BleachNumber = models.CharField(max_length=10, blank=True, null=True)
    Tag_Number = models.CharField(max_length=10, blank=True, null=True)
    Tag_Side = models.ForeignKey(TagSide, blank=True, null=True, on_delete=models.CASCADE)
    Tag_Color = models.ForeignKey(TagColor, blank=True, null=True, on_delete=models.CASCADE)
    ID_Perm = models.CharField(max_length=10, blank=True, null=True)
    Molt = models.BooleanField(blank=True, null=True)
    ID_Description = models.TextField(blank=True, null=True)
    ID_Verified_by = models.CharField(max_length=100, blank=True, null=True)
    SealLogging = models.BooleanField(blank=True, null=True)
    MomPup = models.BooleanField(blank=True, null=True)
    SRA_Set_Up = models.BooleanField(blank=True, null=True)
    SRA_Set_by = models.CharField(max_length=100, blank=True, null=True)
    Volunteers_Engaged = models.IntegerField(blank=True, null=True)
    Seal_Depart = models.BooleanField(blank=True, null=True)
    Seal_Depart_Date = models.DateField(blank=True, null=True)
    Seal_Depart_Time = models.TimeField(blank=True, null=True)
    description = models.TextField()
    animalType = models.ForeignKey(SubAnimal_Table, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, blank=True, null=True)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    CauseOfDeath = models.ForeignKey(Death, blank=True, null=True, on_delete=models.CASCADE)
    Responder = models.CharField(max_length=100, blank=True, null=True)
    Responder_Arrived = models.TimeField(blank=True, null=True)
    Responder_Left = models.TimeField(blank=True, null=True)
    Outreach_Provided = models.BooleanField()
    FAST = models.ForeignKey(FAST, blank=True, null=True, on_delete=models.CASCADE)
    Delivered = models.BooleanField(blank=True, null=True)
    Where_To = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    onIsland = models.ForeignKey(Island, blank=True, null=True, on_delete=models.CASCADE)