# Generated by Django 4.2 on 2023-04-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0004_alter_car_car_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image_one',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
