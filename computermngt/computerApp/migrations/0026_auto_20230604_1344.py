# Generated by Django 2.2.26 on 2023-06-04 13:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0025_auto_20230604_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 4, 13, 44, 39, 791423)),
        ),
    ]
