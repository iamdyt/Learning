from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserManager(AbstractUser):
    choice = (('ND-I','ND-I'),('ND-II','ND-II'),('HND-I','HND-I'),('HND-II','HND-II'))
    result = (('lower','Lower-Credit'),('upper','Upper-Credit'),('pass','Pass'),('distinction','Distinction'))
    is_teacher = models.BooleanField(null=True)
    is_student = models.BooleanField(null=True)
    mobile_number = models.CharField(max_length=13, null=True)
    office = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=8,choices=choice, null=True)
    prev_result = models.CharField(choices=result, max_length=20, null=True)
    image = models.ImageField()