from django.urls import path

from api.views import GeneticTestViewSet


app_name = '%(app_label)s'

urlpatterns = [
    path(
        'tests/',
        GeneticTestViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='tests',
    ),
]
