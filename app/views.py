from django.shortcuts import render
from .models import Recipe
from django.views.decorators.cache import cache_page
from django.core.cache import cache




# @cache_page(600)
@cache_page(60 * 15)
def recipes_view(request):
    recipes = Recipe.objects.all()
    return render(request, 'app/recipes.html', {
        'recipes': recipes
        
    })


def cache_recipes_view(request):
    recipes = cache.get('recipes')
    if recipes is None:
        recipes = Recipe.objects.all()
        cache.set('recipes', recipes)

    return render(request, 'app/recipes.html', {
        'recipes': recipes
    })




