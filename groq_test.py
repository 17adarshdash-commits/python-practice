import os
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

while True:
    user_input = input("You: ")
    
    if user_input == "quit":
        break
    
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": user_input}
    ]
    )
    print(response.choices[0].message.content)