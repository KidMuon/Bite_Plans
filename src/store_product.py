from hash_functions import hash_string
from bs4 import BeautifulSoup

class Store_Product:
    def __init__(self, description):
        if description == '' or not description:
            raise ValueError('Store Products need a description')
        self.description = description
        self.price = None
        self.ingredient = None
    
    def setPrice(self, price):
        self.price = price

    def setIngredient(self, ingredient):
        self.ingredient = ingredient


def load_html_to_database(sdm, file):
    products = products_from_html(file)

    for product in products:
        product_to_database(sdm, product)

def products_from_html(file):
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    product_list = []
    for list_view in soup.select('div[data-testid="list-view"]'):
        sub_soup = list_view
        product = None
        for description in sub_soup.select('span[data-automation-id="product-title"]'):
            product = Store_Product(description.text)
        for price in sub_soup.select('div[data-automation-id="product-price"] > span[class="w_iUH7"]'):
            if 'current price' in price.text:
                try:
                    product.setPrice(float(price.text.strip('current price $')))
                except Exception as e:
                    pass
        product_list.append(product)
    
    return product_list

def product_to_database(sdm, product):
    product_db_table = "Product:"+hash_string(product.description)
    product_db_data = {
            "Product_Description": product.description,
            "Product_Price": product.price,
            "Ingredient": product.ingredient
        }
    sdm.create(product_db_table, product_db_data)

def get_products_from_database(sdm):
    all_database_products = sdm.select("Product")
    product_list = []
    for database_entry in all_database_products:
        product = Store_Product(database_entry["Product_Description"])
        product.setPrice(database_entry.get("Product_Price", None))
        product.setIngredient(database_entry.get("Ingredient", None))
        product_list.append(product)

    return product_list

def predict_ingredient_of_product(llm, ingredients, product):
    user_prompt = "Product Description: " + product.description
    
    system_prompt = "You are going to be given a product description. "
    system_prompt += "Tell me if that product description describes "
    system_prompt += ', '.join(ingredients) + ' or None. '
    system_prompt += "Return the ingredient name that best matches the description. "
    system_prompt += "You can only respond with " + ', '.join(ingredients) + " or None. "
    system_prompt += "Do not say anything else, just the ingredient name exactly as given. "

    return llm.complex_prompt(system_prompt, user_prompt)