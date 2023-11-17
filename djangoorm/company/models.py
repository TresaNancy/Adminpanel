from django.db import models

# # Create your models here.
# class Departments(models.Model):
#     dept_name = models.CharField(max_length=200,null=False)

#     def __str__(self):
#   

class Employee(models.Model):
    name = models.CharField(max_length=200,null=False)
    age = models.IntegerField()
    dept =models.CharField(max_length=200)

    class meta:
        abstract = "True"


    

    def __str__(self):
        return self.name