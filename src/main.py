from local_surreal import SurrealDatabase
from local_llm import LLAMA3
from store_product import *
from ingredient import *
from meal import *

def main():
    SDM = SurrealDatabase()
    LLM = LLAMA3()

    target_recipe = None
    recipes = get_recipes_from_database(SDM)
    for recipe in recipes:
        if recipe.name == 'Bacon, Egg, and Cheese Breakfast Sandwich':
            target_recipe = recipe

    ingredients = get_ingredient_names_from_database(SDM)
    products = get_products_from_database(SDM)
    
    candidate_products = []
    candidate_system_prompt = "I am going to give you a product description from a website."
    candidate_system_prompt += " I need to tell me if this product as described would be useful "
    candidate_system_prompt += " for cooking a '" + target_recipe.name + "'."
    candidate_system_prompt += " If the product describes a meal on it's own, say No."
    candidate_system_prompt += " Please answer only with a Yes or No, nothing else."

    for product in products:
        if not product.ingredient:
            product.ingredient = predict_ingredient_of_product(LLM, ingredients, product)
            product_to_database(SDM, product)
        if product.ingredient in ingredients:
            llama_likes_it = LLM.complex_prompt(candidate_system_prompt, product.description)
            if llama_likes_it == 'Yes':
                candidate_products.append(product)

    store_cart = []
    for ingredient in ingredients:
        ingredient_options = [x for x in candidate_products if x.ingredient == ingredient]
        store_cart.append(sorted(ingredient_options, key=lambda x: x.price)[0])

    print(f"To make: '{target_recipe.name}' \nPurchase the following.")
    total_cost = 0
    for item in store_cart:
        print(item.description)
        total_cost += item.price
    print(f"It will cost ${total_cost}.")
    

if __name__ == '__main__':
    main()