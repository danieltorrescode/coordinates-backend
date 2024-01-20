from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Coordinates

User = get_user_model()


class Coordinate(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    coordinates = Coordinate()

    class Meta:
        model = User
        fields = [
            "first_name",
            "email",
            "coordinates",
        ]
