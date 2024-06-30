from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

class Incidence(models.Model):
    name = models.CharField(max_length=30)
    location = models.PointField(srid=4326)
    objects = GeoManager()

    def __str__(self) -> str:
        return f"{self.name}- {self.location}"
    
class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField(null=True, blank=True)  
    geom = models.MultiPolygonField(srid=4326)
    
    class Meta:
        verbose_name_plural = "Counties"

    
    def __str__(self) -> str:
        return self.counties
