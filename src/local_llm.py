
import ollama, json

class LLAMA3:
    def __init__(self):
        with open('config/llama3.json') as f:
            self.config = json.load(f)
        self.model = 'llama3'

    def _send_prompt(self, system_content, user_content):
        response = ollama.chat(
            model = self.model,
            messages=[
                {'role': 'system', 'content': system_content},
                {'role': 'user', 'content': user_content}
                ]
        )
        return response

    def simple_prompt(self, prompt):
        response = self._send_prompt(None, prompt)
        return response["message"]["content"]

    def describe_recipe_from_name(self, recipe_name):
        response = self._send_prompt(self.config['recipe']['desc_system_prompt'], recipe_name)
        return response["message"]["content"]
    
    def predict_ingredient_from_product_name(self, ingredient_names, product):
        user_prompt = "Ingredients: " + ingredient_names[0]
        for i in range(1, len(ingredient_names)):
            user_prompt += ", " + ingredient_names[i]
        user_prompt = "\n\nProduct Description: " + product
        
        system_prompt = "You are going to be given a product description. "
        system_prompt += "Tell me if that product description describes "
        system_prompt += ', '.join(ingredient_names) + ' or None. '
        system_prompt += "Return the ingredient name that best matches the description. "
        system_prompt += "You can only respond with " + ', '.join(ingredient_names) + " or None. "
        system_prompt += "Do not say anything else, just the ingredient name exactly as given. "

        response = self._send_prompt(system_prompt, user_prompt)
        return response["message"]["content"]