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