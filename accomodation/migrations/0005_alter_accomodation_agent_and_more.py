# Generated by Django 4.0 on 2021-12-18 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_state'),
        ('accomodation', '0004_alter_accomodation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomodation',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listings', to='users.customuser'),
        ),
        migrations.AlterField(
            model_name='accomodationimages',
            name='accomodation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='accomodation.accomodation'),
        ),
    ]
