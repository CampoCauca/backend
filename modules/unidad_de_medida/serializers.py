from rest_framework import serializers
from administracion.models import (
    UnidadDeMedida,
)


class UnidadDeMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadDeMedida
        fields = ["idunidad_de_medida", "nombre", "descripcion"]
