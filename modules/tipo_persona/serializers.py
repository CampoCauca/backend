from rest_framework import serializers
from administracion.models import TipoPersona

class TipoPersonaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TipoPersona
        fields = "__all__"
