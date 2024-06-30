from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Counties, Incidence

    
def index(request):
    return render(request, 'index.html')

def county_datasets(request):
    counties = serialize('geojson',Counties.objects.all())
    return HttpResponse(counties, content_type='json')

def incidences(request):
    points = serialize('geojson',Incidence.objects.all())
    return HttpResponse(points, content_type='json')