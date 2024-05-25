from rest_framework import serializers
from administracion.models import Municipio

class MunicipioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Municipio
        fields = "__all__"