# Generated by Django 4.2 on 2023-04-17 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='email',
            field=models.CharField(default='111', max_length=100),
        ),
    ]
