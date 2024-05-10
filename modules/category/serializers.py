from rest_framework import serializers
from administracion.models import (
    Categoria,
)


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id_categoria", "nombre_categoria", "descipcion_categoria"]
