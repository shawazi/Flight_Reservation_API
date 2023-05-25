from rest_framework import serializers
from .models import Flight, Reservation, Passenger

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"
        
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = "__all__"

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
        extra_kwargs = {"user" : {"read_only" : True}, "flight" : {"required" : True}}