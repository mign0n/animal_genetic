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


class StatisticSerializer(serializers.Serializer):
    species = serializers.CharField()
    total_tests = serializers.IntegerField()
    avg_milk_yield = serializers.FloatField()
    max_milk_yield = serializers.FloatField()
    good_health_percentage = serializers.SerializerMethodField()

    def get_good_health_percentage(self, obj: dict) -> float:
        return (
            obj.get('good_health_count', 0) / obj.get('total_tests', 0) * 100
        )
