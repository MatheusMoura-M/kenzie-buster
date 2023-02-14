from rest_framework import serializers
from .models import Movie, ParentalIndication


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(
        choices=ParentalIndication.choices,
        default=ParentalIndication.DEFAULT,
    )
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(source="user.email", read_only=True)

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
