from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        # fields = "__all__"
        fields = ("id", "model_name", "width", "height", "brand")