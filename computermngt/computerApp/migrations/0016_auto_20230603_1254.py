# Generated by Django 2.2.26 on 2023-06-03 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0015_auto_20230603_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 3, 12, 54, 19, 962349)),
        ),
    ]
