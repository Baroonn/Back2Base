# Generated by Django 4.0 on 2021-12-18 13:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 14, 5, 25, 725474)),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 18, 14, 5, 25, 725474)),
        ),
        migrations.CreateModel(
            name='AccomodationImages',
            fields=[
                ('image_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('accomodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accomodation.accomodation')),
            ],
        ),
    ]
