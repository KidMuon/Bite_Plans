from recipe import Recipe, Ingredient, Measurement
from meal import Meal
from local_surreal import SurrealDatabase
from bs4 import BeautifulSoup
from hash_functions import hash_string

def load_html_to_database(sdm, file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    product_list = []
    for list_view in soup.select('div[data-testid="list-view"]'):
        sub_soup = list_view
        product = {}
        for description in sub_soup.select('span[data-automation-id="product-title"]'):
            product["description"] = description.text
        for price in sub_soup.select('div[data-automation-id="product-price"] > span[class="w_iUH7"]'):
            if 'current price' in price.text:
                try:
                    product["price"] = float(price.text.strip('current price $'))
                except Exception as e:
                    pass
        product_list.append(product)

    for product in product_list:
        product_to_database(sdm, product)

def product_to_database(sdm, product):
    if "price" not in product.keys() or "description" not in product.keys():
        return None
    sdm.create(
        "Product:"+hash_string(product["description"]),
        {
            "Product_Description": product["description"],
            "Product_Price": product["price"]
        }
    )

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