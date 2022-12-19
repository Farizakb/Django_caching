from django.shortcuts import render
from .models import Recipe

# Create your views here.
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipes.html', {
        'recipes': recipes
    })