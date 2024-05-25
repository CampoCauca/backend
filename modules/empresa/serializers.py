from rest_framework import serializers
from administracion.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = "__all__"