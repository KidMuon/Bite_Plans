from hash_functions import hash_string

class Ingredient:
    def __init__(self, ingredient_name):
        self.name = ingredient_name
        self.hash_key = hash_string(self.name)
        self.db_table = 'Ingredient:' + self.hash_key
        self.db_data = {"Name": self.name}

    def __repr__(self):
        return str(self.name)