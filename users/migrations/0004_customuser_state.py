# Generated by Django 4.0 on 2021-12-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_lga_remove_customuser_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='state',
            field=models.CharField(max_length=30, null=True),
        ),
    ]