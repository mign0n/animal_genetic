from rest_framework import serializers

from genetic.models import GeneticTest


class GeneticTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneticTest
        fields = (
            'id',
            'animal_name',
            'species',
            'test_date',
            'milk_yield',
            'health_status',
        )
