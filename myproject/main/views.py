from django.http import JsonResponse
from django.shortcuts import render

from main.models import Patient
from .utils import calculate_distance_score
# Create your views here.
def fetch_nearest(request):
    patient = Patient.objects.first()
    returned = calculate_distance_score(patient=patient)
    return JsonResponse(returned, safe=False)