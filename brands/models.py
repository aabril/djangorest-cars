from django.db import models

# Create your models here.

class Brand(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    brand_name = models.CharField(max_length=30)
    # number_of_cars = 

    def __str__(self):
        return self.brand_name