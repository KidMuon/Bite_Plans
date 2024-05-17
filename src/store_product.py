from hash_functions import hash_string

class Store_Product:
    def __init__(self, description):
        if description == '' or not description:
            raise ValueError('Store Products need a description')
        self.description = description
        self.price = None
        self.ingredient = None
        self.db_table = 'Product:' + hash_string(self.description)
        self.build_db_data()
        
    def build_db_data(self):
        self.db_data = {
            "Description": self.description,
            "Price": self.price,
            "Ingredient": self.ingredient
        }
    
    def setPrice(self, price):
        self.price = price
        self.build_db_data()

    def setIngredient(self, ingredient):
        self.ingredient = ingredient
        self.build_db_data()


