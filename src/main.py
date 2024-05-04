from recipe import Recipe
from local_llm import LLAMA3

LLM = LLAMA3()

bacon_egg = Recipe("Bacon, Egg, and Cheese Breakfast Sandwich")

LLM.generateRecipeDescription(bacon_egg)

print(bacon_egg.description)