from django.shortcuts import render
from .models import Meals


def meals_list(request):
    meal_name = request.GET.get('meal_name')
    ingredients = request.GET.get('ingredients')
    price = request.GET.get('price')
    type = request.GET.get('type')
    cuisine = request.GET.get('cuisine')

    if meal_name and ingredients and price and type and cuisine:
        Meals.objects.create(
            meal_name = meal_name,
            ingredients = ingredients,
            price = price,
            type = type,
            cuisine = cuisine,
        )
    meals = Meals.objects.all()
    ctx = {'meals': meals}
    return render(request, 'meals/meals-list.html', ctx)




