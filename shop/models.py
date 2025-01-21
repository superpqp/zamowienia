from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)
    
    
    
class Orders(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    kod = models.CharField(max_length=200)
