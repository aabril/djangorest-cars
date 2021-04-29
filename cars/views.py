from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Car.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CarSerializer(user)
        return Response(serializer.data)

class CarGenericViewSet(viewsets.GenericViewSet):
    
    def get_queryset(self):
        queryset = Car.objects.all()
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, **kwargs):
        obj = self.get_object()
        serializer = CarSerializer(obj)
        return Response(serializer.data)



class CarModelViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = [IsAdminUser]