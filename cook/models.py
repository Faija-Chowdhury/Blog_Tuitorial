from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Item(models.Model):
    title= models.CharField(max_length=100,blank=False,default=" ")
    video = EmbedVideoField() 
    description =  models.TextField(max_length=700,blank=False,default=" ")

    def __str__(self):
        return self.title 