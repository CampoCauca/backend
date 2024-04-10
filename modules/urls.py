from django.urls import path, include
from rest_framework import routers
from .product.api import ArticuloViewSet


router = routers.DefaultRouter()
router.register(r"products", ArticuloViewSet, "")
# Agregar aqui debajo los demás endopoints con sus respectivos ViewSets

urlpatterns = [
    path("", include(router.urls)),
]
