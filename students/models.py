from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    date_joined = models.DateField(null=True)