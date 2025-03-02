from rest_framework import serializers
from .models import Airplane, Flight, Reservation
import datetime

#In this file,our models are converted to JSON data format that we can access through the API.

#Serializer class that converts the Airplane model to JSON format
class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

#Serializer class that converts the Flight model to JSON format
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate(self, data):
        departure = data.get('departure')
        destination = data.get('destination')
            
        if departure == destination:
            raise serializers.ValidationError("Departure and destination cannot be the same!")

        return data
 
        

#Serializer class that converts the Reservation model to JSON format
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservation
        fields='__all__'
