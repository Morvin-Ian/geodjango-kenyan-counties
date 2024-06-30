from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Incidence, Counties

class IncidenceModelAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location')
    

class CountiesModelAdmin(LeafletGeoAdmin):
    list_display = ('counties', 'codes')

admin.site.register(Incidence, IncidenceModelAdmin)
admin.site.register(Counties, CountiesModelAdmin)