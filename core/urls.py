from django.contrib import admin
from django.urls import path
from app.views import index, county_datasets, incidences

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),    
    path("incidence/", incidences, name='incidence'),
    path("counties/", county_datasets, name='counties')

]
