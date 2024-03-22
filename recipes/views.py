from django.shortcuts import render

from .models import *


# Create your views here.

def index(request):
    categories = Category.objects.all()
    cuisines = Cuisine.objects.all()
    difficulties = Difficulty.objects.all()
    recipes = Recipe.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "cuisines": cuisines,
        "difficulties": difficulties,
        "recipes": recipes
    }

    return render(request, "recipes/index.html", context)


