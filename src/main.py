from recipe import Recipe, Ingredient, Measurement
from meal import Meal
from local_llm import LLAMA3
from local_surreal import SurrealDatabase

def ingredient_to_database(sdm, ingredient):
    sdm.create(ingredient.db_table, ingredient.db_data)

def recipe_to_database(sdm, recipe):
    for _, ingredient in recipe.recipe_ingredients:
        ingredient_to_database(sdm, ingredient)
    sdm.create(recipe.db_table, recipe.db_data)

def meal_to_database(sdm, meal):
    for recipe in meal.meal_parts:
        recipe_to_database(sdm, recipe)
    sdm.create(meal.db_table, meal.db_data)

def main():
    LLM = LLAMA3()

    bacon_egg = Recipe("Bacon, Egg, and Cheese Breakfast Sandwich")
    bacon_egg.addDescription(LLM.describe_recipe_from_name(bacon_egg.name))
    bacon_egg.addIngredient(Ingredient("Bacon"), Measurement(0.125, "lb"))
    bacon_egg.addIngredient(Ingredient("Egg"), Measurement(3, "count"))
    bacon_egg.addIngredient(Ingredient("American Cheese"), Measurement(2, "slice"))
    bacon_egg.addIngredient(Ingredient("Whole Wheat Bread"), Measurement(2, "slice"))
    
    breakfast = Meal("Sunday Morning Breakfast", 1)
    breakfast.addDescription("Breakfast for Sunday, May 5th")
    breakfast.addMealPart(bacon_egg)

    SDM = SurrealDatabase()
    meal_to_database(SDM, breakfast)
    SDM.select("Meal")
    SDM.select("Recipe")
    SDM.select("Ingredient")

if __name__ == '__main__':
    main()