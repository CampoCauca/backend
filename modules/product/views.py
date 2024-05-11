from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from administracion.models import Articulo
from rest_framework import viewsets, permissions
from .serializers import ArticuloSerializer


class ArticuloViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()

        id_persona = self.request.GET.get("idPersona")

        if id_persona:
            queryset = queryset.filter(persona_id_persona=id_persona)

        return queryset
    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "idPersona",
                openapi.IN_QUERY,
                description="ID of the producto",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema(auto_schema=None)
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
