from django.db.models import QuerySet
from django.db.models.aggregates import Avg, Count, Max
from django.db.models.query_utils import Q
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers import GeneticTestsSerializer, StatisticSerializer
from genetic.constants import HealthStatus
from genetic.models import GeneticTest


class GeneticTestViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = GeneticTest.objects.all()
    serializer_class = GeneticTestsSerializer

    def get_queryset(self) -> QuerySet:
        species = self.request.query_params.get('species')
        if not species:
            return self.queryset
        return self.queryset.filter(species=species)

    @action(methods=('GET',), detail=False)
    def statistics(self, request: Request) -> Response:
        return Response(
            StatisticSerializer(
                self.get_queryset()
                .values('species')
                .annotate(
                    total_tests=Count('pk'),
                    avg_milk_yield=Avg('milk_yield'),
                    max_milk_yield=Max('milk_yield'),
                    good_health_count=Count(
                        'pk',
                        filter=Q(health_status=HealthStatus.GOOD),
                    ),
                ),
                many=True,
            ).data,
        )
