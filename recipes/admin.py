from django.contrib import admin

from .models import *


class IngredientInline(admin.TabularInline):
    fk_name = 'recipe'
    model = Ingredient
    extra = 5

class InstructionInline(admin.TabularInline):
    fk_name = 'recipe'
    model = Instruction
    extra = 5


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline]


admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Difficulty)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Instruction)
admin.site.register(CarouselImage)

