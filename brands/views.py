from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Brand
from .serializers import BrandSerializer


class BrandModelViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    # permission_classes = [IsAdminUser]