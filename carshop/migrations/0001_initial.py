# Generated by Django 4.2 on 2023-04-17 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_manufacturer', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('car_price', models.IntegerField()),
                ('car_build_year', models.IntegerField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
