from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# router.register('brand-viewset', views.BrandViewSet, basename='brand_vs')
# router.register('brand-generic-viewset', views.BrandGenericViewSet, basename='brand_gvs')
router.register('brand-model-viewset', views.BrandModelViewSet, basename='brand_mvs')
urlpatterns = router.urls