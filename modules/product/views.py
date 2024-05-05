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

        # Get persona_id_persona from URL parameter

        id_persona = self.request.GET.get("idPersona")

        # Filter queryset based on persona_id_persona
        if id_persona:
            queryset = queryset.filter(persona_id_persona=id_persona)

        return queryset


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
