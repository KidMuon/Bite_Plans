from enum import StrEnum

class Recipe:
    def __init__(self, recipe_name):
        if recipe_name == '':
            raise ValueError('Recipes require names')
        self.name = recipe_name
        self.description = ''
        self.dish_parts = []
        self.servings = 1

    def addIngredient(self, ingredient, measurement):
        self.dish_parts.append((measurement, ingredient))

    def defineServings(self, servings):
        self.servings = servings
    
    def adjustRecipe(self, desired_servings):
        for measurement, ingredient in dish_parts:
            measurement.adjustMeasurement(desired_servings / self.servings)

    def addDescription(self, description = ''):
        self.description = description

class MeasurementNames(StrEnum):
    Teaspoon = 'Teaspoon'
    Tablespoon = 'Tablespoon'
    Cup = 'Cup'
    fl_OZ = 'Fluid Ounce'

class Measurement:
    _measurement_lookup = {
    'tsp': MeasurementNames.Teaspoon,
    'Teaspoon': MeasurementNames.Teaspoon,
    'tbsp': MeasurementNames.Tablespoon,
    'Tablespoon': MeasurementNames.Tablespoon,
    'cup': MeasurementNames.Cup
    }

    def __init__(self, amount_of_measure, measurement):
        self.amount = amount_of_measure
        if _measurement_lookup.get(measurement, None):
            self.measurement = _measurement_lookup.get(measurement, None)
        else:
            raise ValueError("Measurement not in lookup table.")

    def adjustMeasurement(self, scale_factor):
        self.amount *= scale_factor

class Ingredient:
    def __init__(self, ingredient_name):
        self.name = ingredient_name