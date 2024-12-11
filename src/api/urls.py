from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import GeneticTestViewSet

app_name = '%(app_label)s'

router = SimpleRouter()
router.register('tests', GeneticTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
