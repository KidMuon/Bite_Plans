from local_surreal import SurrealDatabase
from local_llm import LLAMA3
from store_product import *
from ingredient import *

def main():
    SDM = SurrealDatabase()
    LLM = LLAMA3()
    
    ingredients = get_ingredient_names_from_database(SDM)
    products = get_products_from_database(SDM)
    
    for product in products:
        product.ingredient = predict_ingredient_of_product(LLM, ingredients, product)
        product_to_database(SDM, product)
    
    print(SDM.select("Product"))

if __name__ == '__main__':
    main()