from django.db import models

# Create your models here.
class contact(models.Model):
    name= models.CharField(max_length=100,blank=False,default=" ")
    email =  models.TextField(max_length=100,blank=False,default=" ")
    subject =  models.TextField(max_length=200,blank=False,default=" ")
    message =  models.TextField(max_length=700,blank=False,default=" ")
    

    def __str__(self):
        return self.subject