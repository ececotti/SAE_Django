# Generated by Django 2.2.26 on 2023-06-04 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computerApp', '0020_auto_20230604_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='maintenanceDate',
            field=models.DateField(default=datetime.datetime(2023, 6, 4, 13, 9, 27, 926612)),
        ),
    ]
