
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

    def simple_prompt(self, user_prompt):
        response = self._send_prompt(None, user_prompt)
        return response["message"]["content"]

    def complex_prompt(self, system_prompt, user_prompt):
        response = self._send_prompt(system_prompt, user_prompt)
        return response["message"]["content"]