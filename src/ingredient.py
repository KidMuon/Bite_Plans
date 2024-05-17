from hash_functions import hash_string
from measurement import *

class Ingredient:
    def __init__(self, ingredient_name):
        self.name = ingredient_name

    def __repr__(self):
        return str(self.name)

def ingredient_to_database(sdm, ingredient):
    ingredient_db_table = 'Ingredient:' + hash_string(ingredient.name)
    ingredient_db_data = {"Name": ingredient.name}
    sdm.create(ingredient_db_table, ingredient_db_data)

def get_ingredients_from_database(sdm):
    all_database_ingredients = sdm.select("Ingredient")
    ingredient_list = []
    for database_entry in all_database_ingredients:
        ingredient = Ingredient(database_entry["Name"])
        ingredient_list.append(ingredient)

    return ingredient_list

def get_ingredient_names_from_database(sdm):
    return [x.name for x in get_ingredients_from_database(sdm)]