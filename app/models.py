from asyncio.windows_events import NULL
from email.policy import default
from statistics import mode
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    def __str__(self):
        return self.name 

class City(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    state = models.ForeignKey(State , on_delete=models.CASCADE , related_name='cities')
    def __str__(self):
        return self.name 

class Hospitals(models.Model):
    name = models.CharField(max_length=50 , null=False , blank=False)
    phone = models.CharField(max_length=12 , null=False , blank=False)
    address = models.CharField(max_length=200 , null=False , blank=False)
    city = models.ForeignKey(City , on_delete=models.CASCADE , related_name='hospitals')
    def __str__(self):
        return self.name 

class Facility(models.Model):
    title = models.CharField(max_length=60,null=False,blank=False,default='')
    def __str__(self):
        return self.title

class Availablity(models.Model):
    hospital = models.ForeignKey(Hospitals,on_delete=models.CASCADE, related_name='availabilities')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='facilities')
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.hospital.name} - {self.facility.title}'

    



