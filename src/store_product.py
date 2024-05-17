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
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    product_list_simple = []
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
        product_list_simple.append(product)

    for product in product_list_simple:
        product_to_database(sdm, product)

def product_to_database(sdm, product):
    product_db_table = "Product:"+hash_string(product.description)
    product_db_data = {
            "Product_Description": product.description,
            "Product_Price": product.price,
            "Ingredient": ""
        }
    sdm.create(product_db_table, product_db_data)