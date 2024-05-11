from django.urls import path, include
from rest_framework import routers
from modules.category.views import CategoriaViewSet
from modules.product.views import ArticuloViewSet, ImagenViewSet
from modules.unidad_de_medida.views import UnidadDeMedidaViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView



router = routers.DefaultRouter()
router.register(r"producto", ArticuloViewSet, basename="producto")
router.register(r"imagenProducto", ImagenViewSet, basename="imagenProducto")
router.register(r"categoria", CategoriaViewSet, basename="categoria")
router.register(r"unidadDeMedida", UnidadDeMedidaViewSet, basename="unidadDeMedida")

schema_view = SpectacularAPIView.as_view()
redoc_view = SpectacularRedocView.as_view(url_name="schema")

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/schema/', schema_view, name='schema'),
    # SpectacularRedocView endpoint
    path('v1/schema/redoc/', redoc_view, name='redoc'),
]
