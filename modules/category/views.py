from rest_framework import viewsets, permissions
from administracion.models import Categoria
from modules.category.serializers import CategoriaSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categoria"], methods=["get"])
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.AllowAny]