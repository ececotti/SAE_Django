# Generated by Django 2.2.26 on 2023-06-06 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0035_auto_20230606_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 21, 34, 41, 171906)),
        ),
    ]
