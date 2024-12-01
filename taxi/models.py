from django.db import models

class Taxi(models.Model):
    taxi_name = models.CharField(max_length=200)
    license_plate = models.CharField(max_length=200)
    driver_name = models.CharField(max_length=200)
    passenger_capacity = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    status = models.CharField(max_length=25)

