from django.contrib import admin
from .models import Recipe,Meal,Ingredient

admin.site.register(Recipe)
admin.site.register(Meal)
admin.site.register(Ingredient)
