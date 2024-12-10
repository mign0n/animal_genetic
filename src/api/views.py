from django.db.models import QuerySet
from rest_framework import mixins, viewsets

from api.serializers import GeneticTestsSerializer
from genetic.models import GeneticTest


class GeneticTestViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = GeneticTest.objects.all()
    serializer_class = GeneticTestsSerializer

    def get_queryset(self) -> QuerySet:
        queryset = GeneticTest.objects.all()
        species = self.request.query_params.get('species')
        if not species:
            return queryset
        return queryset.filter(species=species)
