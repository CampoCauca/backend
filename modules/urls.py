from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from modules.category.views import CategoriaViewSet
from modules.imagenProducto.views import ImagenProductoViewSet
from modules.product.views import ArticuloViewSet
from modules.stock.views import StockViewSet
from modules.users.views import UsersViewSet
from modules.tipo_documento.views import TipoDocumentoViewSet
from modules.empresa.views import EmpresaViewSet
from modules.tipo_persona.views import TipoPersonaViewSet
from modules.municipio.views import MunicipioViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from modules.unidad_de_medida.views import UnidadDeMedidaViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r"producto", ArticuloViewSet, basename="producto")
router.register(r"categoria", CategoriaViewSet, basename="categoria")
router.register(r"unidadDeMedida", UnidadDeMedidaViewSet, basename="unidadDeMedida")
router.register(r"imagenProducto", ImagenProductoViewSet, basename="imagenProducto")
router.register(r"stock", StockViewSet, basename="stock")
router.register(r"usuarios", UsersViewSet, basename="usuarios")
router.register(r"tipoDocumento", TipoDocumentoViewSet, basename="tipoDocumento")
router.register(r"empresa", EmpresaViewSet, basename="empresa")
router.register(r"tipoPersona", TipoPersonaViewSet, basename="tipoPersona")
router.register(r"municipio", MunicipioViewSet, basename="municipio")

# Add other endpoints with their respective ViewSets here

urlpatterns = [
    path("v1/", include(router.urls)),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redocs/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
