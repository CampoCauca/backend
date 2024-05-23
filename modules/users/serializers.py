from rest_framework import serializers
from administracion.models import MyUser


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"