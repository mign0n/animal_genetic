from django.db import models


class HealthStatus(models.TextChoices):
    GOOD = 'good'
    POOR = 'poor'
