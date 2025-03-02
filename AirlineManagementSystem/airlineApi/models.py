from django.core.exceptions import ValidationError
from django.db import models
import random
import string
from django.core.mail import send_mail



#Airplane models created
class Airplane(models.Model):
    tail_number = models.CharField(max_length=10)
    model= models.CharField(max_length=50)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.tail_number

#Flight models created
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights') #An aircraft can be used for multiple flights.


#It provide that there is at least 1 hour difference between flights of an aircraft and that flight times do not conflict.
    def clean(self):
        #Comparing the other flights of the same aircraft
        flights = Flight.objects.filter(airplane=self.airplane).exclude(id=self.id)

        for flight in flights:
            if abs((self.departure_time - flight.arrival_time).total_seconds()) < 3600 or \
               abs((flight.departure_time - self.arrival_time).total_seconds()) < 3600:
                raise ValidationError("Flight times conflicted or are less than 1 hour apart.")

    def save(self, *args, **kwargs):
        self.full_clean()  #Making improvement by calling the clean() method before saving
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.flight_number

#Reservation models created
class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, blank=True) #unique reservation code can be blank in first
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')#flight that is reserved
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            self.reservation_code = self.generate_reservation_code()
            self.full_clean() #run model validation
        super().save(*args, **kwargs)
        self.send_mail()
    
    #generate random and unique reservation code
    def generate_reservation_code(self):
        lenght=random.randint(5,10)#random lenght between 5 and 10
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=lenght))

    #Checking the flight capacity(comparing the aircraft capacity with reservation count)
    def clean(self):
        if self.flight: #if there is a flight
            if self.flight.reservations.count() >= self.flight.airplane.capacity:
                raise ValidationError("Flight capacity is full, you can not reservation.")
        

    #send mail that includes flights informations  to passenger
    def send_mail(self):
        subject="Reservation Informations"
        message=f"""
        Flight Reservation Confirmation:
        {self.flight.flight_number} flight has been reserved for you.
        departure: {self.flight.departure} - arrival: {self.flight.destination}
        Reservation Code:{self.reservation_code}


        Thank you for choosing our airline!
        """
        send_mail(subject,message,'misraayildirm@gmail.com',[self.passenger_email])
    

    def __str__(self):
        return self.reservation_code


