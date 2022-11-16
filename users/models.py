import PIL
from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import models as auth_models
from .manager import UserManager

# Create your models here.

class CustomUser(auth_models.AbstractUser):
    def nameFile(instance, filename):
        return '/'.join(['userimages',str(instance.mobile), filename])

    username = None
    email = models.EmailField(unique=True, primary_key=True)
    mobile = models.CharField(max_length=12)
    name = models.CharField(max_length=25)
    DOB = models.DateField()
    profilepic = models.ImageField(upload_to=nameFile, blank=True) 
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    social_github = models.CharField(max_length=200, blank=True, null=True) 
    social_twitter = models.CharField(max_length=200, blank=True, null=True) 
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  []

    objects = UserManager()

    def __str__(self):
        return self.email

