from rest_framework import viewsets, permissions


from administracion.models import UnidadDeMedida
from modules.unidad_de_medida.serializers import UnidadDeMedidaSerializer


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    permission_classes = [permissions.AllowAny]