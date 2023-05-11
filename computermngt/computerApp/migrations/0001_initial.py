# Generated by Django 4.2 on 2023-05-09 12:19

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Machine",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("name", models.CharField(default="", max_length=6)),
                (
                    "maintenanceDate",
                    models.DateField(
                        default=datetime.datetime(2023, 5, 9, 12, 19, 37, 424400)
                    ),
                ),
                (
                    "mach",
                    models.CharField(
                        choices=[
                            ("PC", "PC - Run windows"),
                            ("Mac", "MAc - Run MacOS"),
                            (
                                "Serveur",
                                "Serveur - Simple Server to deploy virtual machines",
                            ),
                            ("Switch", "Switch − To maintains and connect servers"),
                        ],
                        default="PC",
                        max_length=32,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Personnel",
            fields=[
                (
                    "id",
                    models.PositiveIntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.MaxValueValidator(9999999999999)
                        ],
                    ),
                ),
                ("nom", models.CharField(max_length=200)),
                ("prenom", models.CharField(max_length=200)),
            ],
        ),
    ]