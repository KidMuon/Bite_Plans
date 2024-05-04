from enum import StrEnum
from hash_functions import hash_string

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

class MeasurementNames(StrEnum):
    Teaspoon = 'Teaspoon'
    Tablespoon = 'Tablespoon'
    Cup = 'Cup'
    fl_OZ = 'Fluid Ounce'
    lb = 'lbs'
    Count = 'Count'
    Slice = "Slice"

class Measurement:
    _measurement_lookup = {
    'tsp': MeasurementNames.Teaspoon,
    'Teaspoon': MeasurementNames.Teaspoon,
    'tbsp': MeasurementNames.Tablespoon,
    'Tablespoon': MeasurementNames.Tablespoon,
    'cup': MeasurementNames.Cup,
    'lbs': MeasurementNames.lb,
    'Count': MeasurementNames.Count,
    'Slice': MeasurementNames.Slice
    }

    def __init__(self, amount_of_measure, measurement):
        self.amount = amount_of_measure
        if self._measurement_lookup.get(measurement, None):
            self.measurement = self._measurement_lookup.get(measurement, None)
        else:
            raise ValueError("Measurement not in lookup table.")

    def adjustMeasurement(self, scale_factor):
        self.amount *= scale_factor

class Ingredient:
    def __init__(self, ingredient_name):
        self.name = ingredient_name
        self.hash_key = hash_string(self.name)
        self.db_table = 'Ingredient:' + self.hash_key
        self.db_data = {"Name": self.name}

    def __repr__(self):
        return str(self.name)