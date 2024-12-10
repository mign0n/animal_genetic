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
