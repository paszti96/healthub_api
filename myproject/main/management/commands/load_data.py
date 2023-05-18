from django.core.management.base import BaseCommand
from main.models import Address, Patient, Hospital, HospitalAvailability
import datetime
from random import randint

class Command(BaseCommand):
    help = 'Loads initial data into the database'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Address.objects.all().delete()
        Patient.objects.all().delete()
        Hospital.objects.all().delete()
        HospitalAvailability.objects.all().delete()
        # Creating an address for the patient
        patient_address = Address.objects.create(
            name='Patient Address',
            latitude=47.4979,  # latitude of Budapest
            longitude=19.0402,  # longitude of Budapest
        )

        # Creating a patient
        patient = Patient.objects.create(
            name='Test Patient',
            social_security_num='123-45-6789',
            risk_level=2,
            birth_date='1980-01-01',
            address=patient_address
        )

        # Creating addresses for 5 hospitals
        for i in range(1, 6):
            hospital_address = Address.objects.create(
                name=f'Hospital {i} Address',
                latitude=47.4979 +(randint(-100,100)*0.0001) ,  # latitude of Budapest
                longitude=19.0402 + (randint(-100,100)*0.0001),  # longitude of Budapest
            )
            
            # Creating hospitals
            hospital = Hospital.objects.create(
                name=f'Hospital {i}',
                address=hospital_address
            )

            # Adding availability for each hospital
            
            HospitalAvailability.objects.create(
                hospital=hospital,
                start_time=datetime.datetime(2023,6,1*i),
                end_time=datetime.datetime(2023,6,30-i)
            )

        self.stdout.write(self.style.SUCCESS('Data loaded successfully!'))
