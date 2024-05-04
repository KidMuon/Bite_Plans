
import ollama, json

class LLAMA3:
    def __init__(self):
        with open('config/llama3.json') as f:
            self.config = json.load(f)
        self.model = 'llama3'
        response = simplePrompt('Greetings!')

    def _send_prompt(self, system_content, user_content):
        response = ollama.chat(
            model = self.model,
            messages=[
                {'role': 'system', 'content': system_content},
                {'role': 'user', 'content': user_content}
                ]
        )
        return response

    def simplePrompt(self, prompt):
        response = _send_prompt(None, prompt)
        return response["message"]["content"]

    def generateRecipeDescription(self, recipe):
        response = _send_prompt(self.config['recipe']['desc_system_prompt'])
        recipe.addDescription(response["message"]["content"])
        return None