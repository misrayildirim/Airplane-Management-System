
from rest_framework import generics
from .models import Airplane, Flight, Reservation 
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FlightFilter 
from rest_framework import status

#API endpoints were developed with the **generic view** structures provided by DRF.So reduced code repetition(CBV)


#Airplane ListCreateAPIView
#In this wiew,it is possible to list all airplanes and create new airplane.(GET,POST)
class AirplaneListCreateAPIView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

#Airplane RetrieveUpdateDestroyAPIView
#In this view,it is possible to retrieve(getbyıd), update and delete the airplane with the given id.(GET,PATCH,DELETE)
class AirplaneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    lookup_field = "pk"

#Airplane Flights ListAPIView
#In this view,it is possible to list all flights of the airplane with the given id.(GET)
class AirplaneFlightsListAPIView(generics.ListAPIView):
    serializer_class = FlightSerializer

    def get_queryset(self): #override get_queryset method to filter
        airplane_id = self.kwargs['pk']
        return Flight.objects.filter(airplane_id=airplane_id)

# Flight ListCreateAPIView
##In this wiew,it is possible to list all flights and create new flights.(GET,POST)
class FlightListCreateAPIView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FlightFilter

# Flight RetrieveUpdateDestroyAPIView
#In this view,it is possible to retrieve(getbyıd), update and delete the flight with the given id.(GET,PATCH,DELETE)
class FlightRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# Flight Reservations ListAPIView
#In this view,it is possible to list all reservations of the flight with the given id.(GET)
class FlightReservationsListAPIView(generics.ListAPIView):
    serializer_class = ReservationSerializer

    def get_queryset(self): #override get_queryset method to filter
        flight_id = self.kwargs['pk']
        return Reservation.objects.filter(flight_id=flight_id)

# Reservation ListCreateAPIView
#In this wiew,it is possible to list all reservations and create new reservations.(GET,POST)
class ReservationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# Reservation RetrieveUpdateAPIView
#In this view,it is possible to retrieve(getbyıd) and update the reservation with the given id.(GET,PATCH)
class ReservationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer