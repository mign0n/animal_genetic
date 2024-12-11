from django.db import models

from genetic.constants import HealthStatus


class GeneticTest(models.Model):
    animal_name = models.CharField()
    species = models.CharField()
    test_date = models.DateField()
    milk_yield = models.FloatField()
    health_status = models.CharField(choices=HealthStatus.choices)
    created_at = models.DateTimeField(auto_now=True)
