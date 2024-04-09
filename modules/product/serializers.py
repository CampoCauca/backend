from rest_framework import serializers
from administracion.models import Articulo


class ArticuloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Articulo
        fields = (
            "id_articulo",
            "nombre_articulo",
            "descripcion_articulo",
            "imagen",
            "categoria_id_categoria",
            "unidad_de_medida_idunidad_de_medida",
        )
