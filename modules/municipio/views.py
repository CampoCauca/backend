from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, permissions
from administracion.models import Municipio
from modules.municipio.serializers import MunicipioSerializer

class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "idtipo_documento",
                openapi.IN_QUERY,
                description="Id of municipio",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, pk, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, pk, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)