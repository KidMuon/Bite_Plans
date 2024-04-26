from recipe import Recipe

class Meal:
    def __init__(self, meal_name, servings, meal_description = ''):
        self.name = meal_name
        self.servings = servings
        self.description = meal_description
        self.meal_parts = []

    def addDescription(self, meal_description):
        self.description = meal_description

    def addMealPart(self, recipe):
        meal_part = recipe
        self.meal_parts.append(meal_part.adjustRecipe(self.servings))