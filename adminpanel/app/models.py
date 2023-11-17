from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    

    def __str__(self) :
        return self.name
    


# class Admin(models.Model):
#     username=models.CharField(max_length=100,unique=True)
#     password=models.CharField(max_length=50)
