from datetime import date
from math import degrees
from django.db import models
from django.forms import NullBooleanField

# Create your models here.
class Customers(models.Model):
    customername = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,unique=True)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    meternum= models.BigIntegerField(unique=True,default=None)
    previousunit= models.BigIntegerField(default=0)
    currentunit= models.BigIntegerField(default=0)
    discountamount=models.BigIntegerField(default=0)
    fineamount=models.BigIntegerField(default=0)
    totaldue=models.BigIntegerField(default=0)

class Users(models.Model):
    email = models.EmailField(primary_key=True)
    citizenship = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

class Rates(models.Model):
    rate= models.IntegerField(default=0)
    fine=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)

class Revenue(models.Model):
    date = models.DateField()
    amount = models.BigIntegerField(default=0)