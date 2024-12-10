# Generated by Django 5.1.4 on 2024-12-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='GeneticTest',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('animal_name', models.CharField()),
                ('species', models.CharField()),
                ('test_date', models.DateField()),
                ('milk_yield', models.FloatField()),
                ('health_status', models.CharField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
