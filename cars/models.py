from django.db import models

class Brand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    brand_name = models.CharField(max_length=30)
    # number_of_cars = 

class Car(models.Model):
    model_name = models.CharField(max_length=30)
    width = models.FloatField()
    height = models.FloatField()
    # belongs_to = reference to Brand

