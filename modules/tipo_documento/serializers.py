from rest_framework import serializers
from administracion.models import TipoDocumento


class TipoDocumentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoDocumento
        fields = "__all__"