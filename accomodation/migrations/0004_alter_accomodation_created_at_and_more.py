# Generated by Django 4.0 on 2021-12-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0003_alter_accomodation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='accomodation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]