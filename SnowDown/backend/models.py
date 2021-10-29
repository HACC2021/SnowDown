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
    
    def __str__(self):
        return self.animal
    
# Animal Sub category
class SubAnimal_Table(models.Model):
    subAnimal = models.CharField(max_length=400, unique=True)
    animal = models.ForeignKey(Animal_Table, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.animal.__str__() + ', ' + self.subAnimal.__str__()

# Animal Characteristics
class Animal_Characteristics_Table(models.Model):
    characteristicsTag = models.CharField(max_length=400, unique=True)

class Incident_Photos_Table(models.Model):
    photo = models.ImageField(upload_to='Report_Images/')

# Holds the Incidents people have reported
class Incident_Table(models.Model):
    dateTime = models.DateTimeField()
    lat = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    lng = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    location = models.CharField(max_length=500)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=18)
    email = models.CharField(max_length=500)
    animal = models.ForeignKey(SubAnimal_Table, on_delete=models.CASCADE)
    description = models.TextField()
    photos = models.ManyToManyField(Incident_Photos_Table)
    characteristics = models.ManyToManyField(Animal_Characteristics_Table)
    people = models.IntegerField()
    
class Incident_Before_Photos_Table(models.Model):
    photo = models.ImageField(upload_to='Volunteer_Before_Images/')
    
class Incident_After_Photos_Table(models.Model):
    photo = models.ImageField(upload_to='Volunteer_After_Images/')
    
class Group_Incident_Table(models.Model):
    incident = models.ManyToManyField(Incident_Table)
    upLat = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    downLat = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    leftLng = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    rightLng = models.DecimalField(max_digits=19, decimal_places=15, db_index=True)
    description = models.TextField()
    procedureDone = models.TextField()
    pictureBefore = models.ManyToManyField(Incident_Before_Photos_Table)
    pictureAfter = models.ManyToManyField(Incident_After_Photos_Table)
    timeArrived = models.DateTimeField()
    timeLeft = models.DateTimeField()
    volunteerCheck = models.BooleanField(default=False)
    volunteer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)