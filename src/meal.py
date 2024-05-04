from recipe import Recipe
from hash_functions import hash_string

class Meal:
    def __init__(self, meal_name, servings, meal_description = ''):
        self.name = meal_name
        self.servings = servings
        self.description = meal_description
        self.meal_parts = []
        self.db_table = 'Meal:' + hash_string(self.name)
        self.db_data = {
            "Name": self.name,
            "Description": self.description,
            "Meal_Parts": [],
            "Servings": self.servings
        }

    def addDescription(self, meal_description):
        self.description = meal_description
        self.db_data["Description"] = self.description

    def addMealPart(self, recipe):
        insert_recipe = recipe
        insert_recipe.changeServings(self.servings)
        self.meal_parts.append(insert_recipe)
        self.db_data["Meal_Parts"].append(recipe.name)