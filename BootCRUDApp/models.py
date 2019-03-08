from django.db import models

# Create your models here.

class Garage(models.Model):
    name = models.CharField(max_length=200, default = "")
    description = models.TextField(max_length=5000000, default = "")
    price = models.IntegerField(default=0)
    itemPicture = models.CharField(max_length=900, default="")

