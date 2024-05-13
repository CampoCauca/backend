from rest_framework import serializers
from administracion.models import (
    Imagen,
)


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = "__all__"
