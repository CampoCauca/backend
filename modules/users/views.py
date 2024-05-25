from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework import viewsets, permissions
from administracion.models import Persona
from modules.users.serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id_persona",
                openapi.IN_QUERY,
                description="Id of user",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema()
    def update(self, request, pk, *args, **kwargs):
        return super().update(request, pk, *args, **kwargs)

    @swagger_auto_schema()
    def partial_update(self, request, pk, *args, **kwargs):
        return super().partial_update(request, pk, *args, **kwargs)

    @swagger_auto_schema()
    def destroy(self, request, pk, *args, **kwargs):
        return super().destroy(request, pk, *args, **kwargs)

    @swagger_auto_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)