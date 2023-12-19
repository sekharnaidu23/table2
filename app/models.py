from django.db import models

# Create your models here.
class Country(models.Model):
    CID=models.IntegerField(primary_key=True)
    CNAME=models.CharField(max_length=100)
    
