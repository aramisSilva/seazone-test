from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ImovelViewSet

router = DefaultRouter()
router.register('imoveis', ImovelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]