from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('api/brand/?', views.BrandList.as_view()),
    path('api/brand/<int:pk>/?', views.BrandDetail.as_view()),
    path('api/model/?', views.ModelList.as_view()),
    path('api/model/<int:pk>/?', views.ModelDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)