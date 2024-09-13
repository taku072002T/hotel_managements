from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer


# Create your views here.


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def delete(request, *args, **kwargs):
        Hotel.objects.all().delete()
        return Response()

