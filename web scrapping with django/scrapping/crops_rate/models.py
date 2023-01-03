from django.db import models

# Create your models here.

class OnionRate(models.Model):
    crop_name = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)
    total_onion = models.IntegerField()
    minimum_rate = models.IntegerField()
    maximum_rate = models.IntegerField()
    # row_date = models.CharField(max_length=40)
    date = models.DateField(unique=True)

    
