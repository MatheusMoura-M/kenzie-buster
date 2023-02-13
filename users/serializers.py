from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User
import ipdb


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=25,
        validators=[
            UniqueValidator(User.objects.all(), message="username already taken.")
        ],
    )
    email = serializers.CharField(
        max_length=127,
        validators=[
            UniqueValidator(User.objects.all(), message="email already registered.")
        ],
    )
    password = serializers.CharField(max_length=25, write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
