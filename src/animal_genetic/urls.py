from django.apps import apps
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(
        '',
        include('api.urls', namespace=apps.get_app_config('api').name),
        name='api',
    ),
    path('admin/', admin.site.urls),
]
