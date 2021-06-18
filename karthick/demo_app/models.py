from django.db import models
from django.db.models.fields import DateTimeField


# Create your models here.
class demo(models.Model):
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=50)
class details(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    age=models.CharField(max_length=25)
    
class Meta:
    db_table="details"    
class Student_details(models.Model):
    name=models.CharField(max_length=100)
    Dept=models.CharField(max_length=50)
    Date_of_birth=models.DateTimeField(DateTimeField)
    contact=models.CharField(max_length=100)
    address=models.TextField(max_length=50)
class Meta:
    db_table="Student_details"    

