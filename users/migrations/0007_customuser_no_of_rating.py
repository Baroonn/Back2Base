# Generated by Django 4.0 on 2021-12-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='no_of_rating',
            field=models.IntegerField(default=0),
        ),
    ]
