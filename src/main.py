from local_surreal import SurrealDatabase

def main():
    SDM = SurrealDatabase()
    SDM.select("Meal")
    SDM.select("Recipe")
    SDM.select("Ingredient")
    SDM.select("Product")

if __name__ == '__main__':
    main()