from rest_framework import serializers
from cars import models

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = (
            'model_name'
        )
        model = models.Car

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'brand_name',
            'created_at'
        )
        model = models.Brand