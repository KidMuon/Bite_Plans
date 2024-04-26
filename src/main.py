import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": "Give me a detailed description of Gandalf's relationship with Bilbo Baggins",
        }
    ],
)

print(response["message"]["content"])
