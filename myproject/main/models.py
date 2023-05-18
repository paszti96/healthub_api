from django.db import models
from math import sqrt
# Create your models here.
class Address(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def calculate_distance(self, other):
        return sqrt((self.latitude-other.latitude)**2 + (self.longitude-other.longitude)**2)

class Patient(models.Model):
    name = models.CharField(max_length=255)
    social_security_num = models.CharField(max_length=11, unique=True)
    risk_level = models.IntegerField()
    birth_date = models.DateField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class HospitalAvailability(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='availabilities')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    timeslot = models.DateTimeField()

