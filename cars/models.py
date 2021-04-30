from django.db import models
from brands.models import Brand

class Car(models.Model):
    model_name = models.CharField(max_length=30)
    width = models.FloatField()
    height = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ['model_name']
