from recipe import Recipe, Ingredient, Measurement
from meal import Meal
from local_llm import LLAMA3
from local_surreal import SurrealDatabase
from load_database import *
from static_html import *

def main():
    LLM = LLAMA3()
    SDM = SurrealDatabase()

    skip_if_populated = True
    if len(SDM.select("Meal")) > 0 and skip_if_populated:
        print("Database already populated with test data... Skipping...")
        return

    bacon_egg = Recipe("Bacon, Egg, and Cheese Breakfast Sandwich")
    bacon_egg.addDescription(LLM.describe_recipe_from_name(bacon_egg.name))
    bacon_egg.addIngredient(Ingredient("Bacon"), Measurement(0.125, "lb"))
    bacon_egg.addIngredient(Ingredient("Egg"), Measurement(3, "count"))
    bacon_egg.addIngredient(Ingredient("American Cheese"), Measurement(2, "slice"))
    bacon_egg.addIngredient(Ingredient("Whole Wheat Bread"), Measurement(2, "slice"))

    breakfast = Meal("Sunday Morning Breakfast", servings=1)
    breakfast.addDescription("Breakfast for Sunday, May 5th")
    breakfast.addMealPart(bacon_egg)

    meal_to_database(SDM, breakfast)

    for file in list_html_files('html_files'):
        load_html_to_database(SDM, file)


if __name__ == '__main__':
    main()