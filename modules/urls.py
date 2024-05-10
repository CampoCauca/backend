from django.urls import path, include
from rest_framework import routers
from modules.product.views import ArticuloViewSet, ImagenViewSet, CategoriaViewSet
from modules.unidad_de_medida.views import UnidadDeMedidaViewSet


router = routers.DefaultRouter()
router.register(r"producto", ArticuloViewSet, basename="producto")
router.register(r"imagenProducto", ImagenViewSet, basename="imagenProducto")
router.register(r"categoria", CategoriaViewSet, basename="categoria")
router.register(r"unidadDeMedida", UnidadDeMedidaViewSet, basename="unidadDeMedida")
# Add other endpoints with their respective ViewSets here

urlpatterns = [
    path('v1/', include(router.urls)),
]
