from django.db import models

class Brand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    brand_name = models.CharField(max_length=30)
    # number_of_cars = 

    def __str__(self):
        return self.brand_name

class Car(models.Model):
    model_name = models.CharField(max_length=30)
    width = models.FloatField()
    height = models.FloatField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.model_name

    class Meta:
        ordering = ['model_name']
