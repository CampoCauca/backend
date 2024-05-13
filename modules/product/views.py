from administracion.models import Articulo, Categoria, Movimiento, Stock, UnidadDeMedida, Imagen
from rest_framework import viewsets, permissions
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
        print(queryset)

        # Get persona_id_persona from URL parameter

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
