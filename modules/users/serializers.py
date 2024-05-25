from rest_framework import serializers
from administracion.models import Persona


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = "__all__"