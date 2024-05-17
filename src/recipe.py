from hash_functions import hash_string
from measurement import Measurement
from ingredient import Ingredient

class Recipe:
    def __init__(self, recipe_name):
        if recipe_name == '':
            raise ValueError('Recipes require names')
        self.name = recipe_name
        self.description = ''
        self.recipe_ingredients = []
        self.servings = 1
        self.db_table = 'Recipe:' + hash_string(self.name)
        self.db_data = {
            "Name": self.name, 
            "Description": self.description, 
            "Ingredients": [],
            "Servings": self.servings
        }

    def addIngredient(self, ingredient, measurement):
        self.recipe_ingredients.append((measurement, ingredient))
        self.db_data["Ingredients"].append(str(ingredient))

    def defineServings(self, servings):
        self.servings = servings
        self.db_data["Servings"] = self.servings
    
    def changeServings(self, desired_servings):
        for measurement, ingredient in self.recipe_ingredients:
            measurement.adjustMeasurement(desired_servings / self.servings)

    def addDescription(self, description = ''):
        self.description = description
        self.db_data["Description"] = self.description