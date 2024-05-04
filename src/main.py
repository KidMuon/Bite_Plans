from recipe import Recipe, Ingredient, Measurement
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
    # meal to database

def main():
    LLM = LLAMA3()

    bacon_egg = Recipe("Bacon, Egg, and Cheese Breakfast Sandwich")
    bacon_egg.addDescription(LLM.describe_recipe_from_name(bacon_egg.name))
    bacon_egg.addIngredient(Ingredient("Bacon"), Measurement(0.125, "lbs"))
    bacon_egg.addIngredient(Ingredient("Egg"), Measurement(3, "Count"))
    bacon_egg.addIngredient(Ingredient("American Cheese"), Measurement(2, "Slice"))
    bacon_egg.addIngredient(Ingredient("Whole Wheat Bread"), Measurement(2, "Slice"))

    SDM = SurrealDatabase()
    recipe_to_database(SDM, bacon_egg)
    SDM.select("Recipe")
    SDM.select("Ingredient")

if __name__ == '__main__':
    main()