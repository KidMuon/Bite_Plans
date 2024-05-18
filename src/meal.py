from recipe import *
from hash_functions import hash_string

class Meal:
    def __init__(self, meal_name, servings, meal_description = ''):
        self.name = meal_name
        self.servings = servings
        self.description = meal_description
        self.meal_parts = []

    def addDescription(self, meal_description):
        self.description = meal_description

    def addMealPart(self, recipe):
        insert_recipe = recipe
        insert_recipe.changeServings(self.servings)
        self.meal_parts.append(insert_recipe)

def meal_to_database(sdm, meal):
    for recipe in meal.meal_parts:
        recipe_to_database(sdm, recipe)

    meal_db_table = 'Meal:' + hash_string(meal.name)
    recipe_names = [recipe.name for recipe in meal.meal_parts]
    meal_db_data = {
        "Name": meal.name,
        "Description": meal.description,
        "Meal_Parts": recipe_names,
        "Servings": meal.servings
    }

    sdm.create(meal_db_table, meal_db_data)

def get_meals_from_database(sdm):
    meal_list = []
    for database_entry in sdm.select('Meal'):
        meal = Meal(database_entry["Name"], database_entry["Servings"], database_entry["Description"])
        
        meal_list.append(meal)

    return meal_list