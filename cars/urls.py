from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('car-viewset', views.CarViewSet, basename='car_vs')
router.register('car-generic-viewset', views.CarGenericViewSet, basename='car_gvs')
router.register('car-model-viewset', views.CarModelViewSet, basename='car_mvs')
urlpatterns = router.urls