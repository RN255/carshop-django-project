from django.db import models

# Create your models here.

class Car(models.Model):
    car_manufacturer = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_price =  models.IntegerField()
    car_build_year =  models.IntegerField()
    car_description =  models.TextField(null=True, blank=True)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.car_manufacturer + " " + self.car_model + " " + str(self.car_build_year)
