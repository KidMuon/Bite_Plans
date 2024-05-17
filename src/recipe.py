from hash_functions import hash_string
from ingredient import *
from measurement import *

class Recipe:
    def __init__(self, recipe_name):
        if recipe_name == '':
            raise ValueError('Recipes require names')
        self.name = recipe_name
        self.description = ''
        self.recipe_ingredients = []
        self.servings = 1

    def addIngredient(self, ingredient, measurement):
        self.recipe_ingredients.append((measurement, ingredient))

    def defineServings(self, servings):
        self.servings = servings
    
    def changeServings(self, desired_servings):
        for measurement, ingredient in self.recipe_ingredients:
            measurement.adjustMeasurement(desired_servings / self.servings)

    def addDescription(self, description = ''):
        self.description = description

def recipe_to_database(sdm, recipe):
    for _, ingredient in recipe.recipe_ingredients:
        ingredient_to_database(sdm, ingredient)

    recipe_db_table = 'Recipe:' + hash_string(recipe.name)
    recipe_ingredients = [ingredient[1].name for ingredient in recipe.recipe_ingredients]
    recipe_db_data = {
            "Name": recipe.name, 
            "Description": recipe.description, 
            "Ingredients": recipe_ingredients,
            "Servings": recipe.servings
        }

    sdm.create(recipe_db_table, recipe_db_data)

def describe_recipe_with_LLM(llm, recipe):
    system_prompt = "You are being passed the name of a recipe."
    system_prompt += " Generate a short and appetizing description of the meal."
    system_prompt += " Do not include any greeting."
    recipe.addDescription(llm.complex_prompt(system_prompt, recipe.name))