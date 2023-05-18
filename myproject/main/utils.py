from main.models import Patient, Hospital
from django.utils import timezone
import heapq
from django.db.models import Min

def calculate_distance_score(patient):
        # Get all hospitals along with their earliest available date
        hospitals = Hospital.objects.annotate(earliest_availability=Min('availabilities__start_time'))

        # Initialize the minimum distance and nearest hospital
        nearest_hospitals = []

        for hospital in hospitals:
            # Calculate the distance between the patient's address and the current hospital
            availability_in_days = (hospital.earliest_availability- timezone.now()).days
            distance = patient.address.calculate_distance(hospital.address)
            distance_score =distance* availability_in_days
            heapq.heappush(
                  nearest_hospitals, (
                    distance_score, 
                    availability_in_days, 
                    distance,
                    hospital
                )
            )
        
        # score = patient.risk_level / min_distance
        nearest =  heapq.nsmallest(iterable=nearest_hospitals,n=5)
        retval = []
        for hospital in nearest:
              retval.append(
                    {   
                        'hospital': hospital[3].name,
                        'address': hospital[3].address.name,
                        'earliest_appointment': hospital[3].earliest_availability,
                        'waiting_time': hospital[1]         # in days
                    }
              )
        return retval