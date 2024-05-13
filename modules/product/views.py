from drf_yasg.utils import swagger_auto_schema

from administracion.models import Articulo
from rest_framework import viewsets, permissions
from .serializers import ArticuloSerializer
from .serializers import (
    ArticuloSerializer,
    CategoriaSerializer,
    MovimientoSerializer,
    StockSerializer,
    UnidadDeMedidaSerializer,
    ImagenSerializer
)

from .domain.criteria.criterias import PriceCriteria, StockCriteria, NameCriteria, CategoryCriteria

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    permission_classes = [permissions.AllowAny]


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        idPersona = self.request.GET.get("idPersona") # Obligatorio
        paramCriteria = self.request.GET.get("criteria")
        paramCriteriaValue = self.request.GET.get("value")

        # Filter queryset based on persona_id_persona
        if idPersona:
            queryset = queryset.filter(persona_id_persona=idPersona)
        
        match paramCriteria:
            case "min_price":
                criteria = PriceCriteria(paramCriteriaValue)
            case "stock":
                criteria = StockCriteria(paramCriteriaValue)
            case "name":
                criteria = NameCriteria(paramCriteriaValue)
            case "category":
                criteria = CategoryCriteria(paramCriteriaValue)
            case default:
                return queryset

        return criteria.apply(queryset)

class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
    permission_classes = [permissions.AllowAny]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.AllowAny]
    
    
class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    permission_classes = [permissions.AllowAny]
    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
