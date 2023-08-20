from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rental
from .serializers import RentalSerializer
from django.db.models import Count
from django.db.models.functions import TruncMonth
from rest_framework.decorators import api_view

class RentalList(APIView):
    def get(self, request, format=None):
        rentals = Rental.objects.all().order_by('return_date', 'rental_date')
        serializer = RentalSerializer(rentals, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def monthly_rental_stats(request):
    monthly_stats = (
        Rental.objects
        .annotate(month=TruncMonth('rental_date'))
        .values('month')
        .annotate(rental_count=Count('id'))
        .order_by('month')
    )

    data = {item['month'].strftime('%Y-%m'): item['rental_count'] for item in monthly_stats}
    return Response(data)
@api_view(['GET'])
def popular_rental_station(request):
    stations = (
        Rental.objects
        .values('vehicle__vehicleatrentalstation__rental_station__name')
        .annotate(rental_count=Count('id'))
        .order_by('-rental_count')
    )

    data = {item['vehicle__vehicleatrentalstation__rental_station__name']: item['rental_count'] for item in stations}
    return Response(data)

@api_view(['GET'])
def popular_vehicle_type(request):
    vehicle_types = (
        Rental.objects
        .values('vehicle__vehicle_type__name')
        .annotate(rental_count=Count('id'))
        .order_by('-rental_count')
    )

    data = {item['vehicle__vehicle_type__name']: item['rental_count'] for item in vehicle_types}
    return Response(data)
