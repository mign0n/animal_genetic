# Generated by Django 5.1.4 on 2024-12-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genetic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genetictest',
            name='health_status',
            field=models.CharField(
                choices=[('good', 'Good'), ('poor', 'Poor')]
            ),
        ),
    ]
