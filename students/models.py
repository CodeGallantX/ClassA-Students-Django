from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    date_joined = models.DateField(null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    

class Profiles(models.Model):
    username = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='pictures')
    class Meta:
        db_table = "profile"

