from rest_framework import serializers
from cars import models

class ModelSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = (
            '__all__'
        )
        model = models.Model

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'brand_name',
            'created_at'
        )
        model = models.Brand