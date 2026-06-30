import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

your_text_here = "Cricket is one of the most popular sports in India, with a massive following across all age groups. The Indian Premier League, known as IPL, has turned the sport into a major entertainment business with huge viewership and sponsorship deals. Young players often dream of representing their state teams before making it to the national level. Domestic tournaments like the Ranji Trophy serve as a key stepping stone for aspiring cricketers."

prompt = f"""Summarize this text and return ONLY valid JSON, no other text, in this exact format:
{{"summary": "...", "key_points": ["...", "...", "..."]}}

Text: {your_text_here}"""

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

raw_text = response.choices[0].message.content

result = json.loads(raw_text)
print(result["summary"])