from rest_framework import serializers
from . import models
from .models import Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'name', 'prefecture', 'city', 'postnumber', 'created_at')
        read_only_fields = ('id',)
