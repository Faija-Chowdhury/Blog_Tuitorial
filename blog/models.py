from django.db import models

# Create your models here.
class about(models.Model):
    title= models.CharField(max_length=100,blank=False,default=" ")
    image = models.ImageField(upload_to='about/',blank=False,default=" ")
    description =  models.TextField(max_length=700,blank=False,default=" ")
    

    def __str__(self):
        return self.title

class slider(models.Model):
    title= models.CharField(max_length=100,blank=False,default=" ")
    image = models.ImageField(upload_to='slider/',blank=False,default=" ")
    description =  models.TextField(max_length=700,blank=False,default=" ")

    def __str__(self):
        return self.title

class privacy(models.Model):
    title= models.CharField(max_length=100,blank=False,default=" ")
    Update= models.CharField(max_length=80,blank=False,default=" ")
    description =  models.TextField(max_length=12000,blank=False,default=" ")

    def __str__(self):
        return self.title

class term(models.Model):
    title= models.CharField(max_length=100,blank=False,default=" ")
    description =  models.TextField(max_length=12000,blank=False,default=" ")

    def __str__(self):
        return self.title
