from django.db import models#module is used to define the structure of our database tables.

# Create your models here.
class Mobilemodel(models.Model):
    #This line creates a new class named Mobilemodel, which is a subclass of models.Model
    name=models.CharField(max_length=20)#It is used to store the name of the mobile phone.
    brand=models.CharField(max_length=20)#this field is used to store the brand of the mobile phone.
    price=models.IntegerField(null=True)# This is an integer field (IntegerField) that can store the price of the mobile phone
    year=models.PositiveIntegerField(null=True)# these fields are allowed to have a null (or empty) value in the database.
    color=models.CharField(max_length=20)#
