# Generated by Django 4.0 on 2021-12-17 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]