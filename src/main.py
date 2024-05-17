from local_surreal import SurrealDatabase
from local_llm import LLAMA3

def main():
    SDM = SurrealDatabase()
    LLM = LLAMA3()
    
    ingredients = [x['Name'] for x in SDM.get_column_from_table("Name", "Ingredient")]
    print(ingredients)
    products = SDM.get_column_from_table(["id", "Product_Description"], "Product")
    print(products)
    '''
    matched_results = []
    data = {}
    for product in products:
        matched_prod_descriptions = {}
        matched_prod_descriptions["Table"] = product['id']
        matched_prod_descriptions["Description"] = product['Product_Description']
        matched_prod_descriptions["Classification"] = LLM.predict_ingredient_from_product_name(ingredients, product['Product_Description'])
        matched_results.append(matched_prod_descriptions)
        update_data = {'Ingredient': matched_prod_descriptions["Classification"]}
        SDM.update(matched_prod_descriptions["Table"], update_data)

    for result in matched_results:
        print(result)
    '''
    
    print(SDM.select("Product"))

if __name__ == '__main__':
    main()