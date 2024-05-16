from local_surreal import SurrealDatabase
from local_llm import LLAMA3

def main():
    SDM = SurrealDatabase()
    LLM = LLAMA3()
    
    ingredients = SDM.get_column_from_table("Name", "Ingredient")
    #print(ingredients)
    products = SDM.get_column_from_table(["id", "Product_Description"], "Product")
    print(products)

    '''
    matched_results = []
    for product in products:
        matched_prod_descriptions = {}
        matched_prod_descriptions["Description"] = product
        matched_prod_descriptions["Classification"] = LLM.predict_ingredient_from_product_name(ingredients, product)
        matched_results.append(matched_prod_descriptions)

    for result in matched_results:
        print(result)
    '''

if __name__ == '__main__':
    main()