from django.db import models

class Meals(models.Model):
    meal_name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=25)
    cuisine = models.CharField(max_length=100)
