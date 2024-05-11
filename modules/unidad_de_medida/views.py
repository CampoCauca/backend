from rest_framework import viewsets, permissions
from drf_yasg.utils import swagger_auto_schema


from administracion.models import UnidadDeMedida
from modules.unidad_de_medida.serializers import UnidadDeMedidaSerializer


class UnidadDeMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadDeMedida.objects.all()
    serializer_class = UnidadDeMedidaSerializer
    permission_classes = [permissions.AllowAny]
    
    
    @swagger_auto_schema(auto_schema=None)  # Hide entire method (create)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)  # Hide entire method (update)
    def update(self, request, pk, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)  # Hide entire method (partial_update)
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)  # Hide entire method (destroy)
    def destroy(self, request, pk, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)  # Hide entire method (destroy)
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)