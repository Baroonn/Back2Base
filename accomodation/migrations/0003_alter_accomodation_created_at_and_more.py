# Generated by Django 4.0 on 2021-12-18 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0002_alter_accomodation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 14, 5, 58, 867059)),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 14, 5, 58, 867059)),
        ),
    ]
