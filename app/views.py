from django.shortcuts import render
from .models import Recipe
from django.views.decorators.cache import cache_page


@cache_page(600)
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipes.html', {
        'recipes': recipes
        
    })