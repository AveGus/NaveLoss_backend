
from rest_framework import serializers
from carlocation.models import CarInfo


class CarModel:
    def __init__(self, user, latitude, longitude, comment):
        self.user = user
        self.latitude = latitude
        self.longitude = longitude
        self.comment = comment


class CarInfoSerializer(serializers.Serializer):
    user = serializers.CharField()
    latitude = serializers.CharField()
    longitude = serializers.CharField()
    comment = serializers.CharField()

    def create(self, validated_data):
        return CarInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for argument in validated_data:
            setattr(instance, argument, validated_data[argument])
        instance.save()
        return instance

