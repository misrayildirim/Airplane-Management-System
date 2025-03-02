from django.urls import path
from . import views

urlpatterns = [
    path('airplanes/', views.AirplaneListCreateAPIView.as_view(), name='airplane-list'),
    path('airplanes/<int:pk>/', views.AirplaneRetrieveUpdateDestroyAPIView.as_view(), name='airplane-detail'),
    path('airplanes/<int:pk>/flights/', views.AirplaneFlightsListAPIView.as_view(), name='airplane-flights'),
    path('flights/', views.FlightListCreateAPIView.as_view(), name='flight-list'),
    path('flights/<int:pk>/', views.FlightRetrieveUpdateDestroyAPIView.as_view(), name='flight-detail'),
    path('flights/<int:pk>/reservations/', views.FlightReservationsListAPIView.as_view(), name='flight-reservations'),
    path('reservations/', views.ReservationListCreateAPIView.as_view(), name='reservation-list'),
    path('reservations/<int:pk>/', views.ReservationRetrieveUpdateAPIView.as_view(), name='reservation-detail'),
    
]