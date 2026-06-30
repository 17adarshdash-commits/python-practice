from flask import Flask, jsonify, request
from flask_cors import CORS
from groq import Groq
import os
import json

app = Flask(__name__)
CORS(app)
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Hello World"

@app.route('/about')
def about():
    return jsonify({"name": "Adarsh", "role": "Student"})

@app.route('/fake')
def fake():
    tasks = [
        {"task": "Gym", "completed": "yes"},
        {"task": "Office", "completed": "no"},
        {"task": "Home", "completed": "no"}
    ]
    return jsonify(tasks)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    
    prompt = f"""Summarize this text and return ONLY valid JSON, no other text, in this exact format:
{{"summary": "...", "key_points": ["...", "...", "..."]}}

Text: {text}"""
    
    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
    )
    rt = response.choices[0].message.content
    result = json.loads(rt)
    return jsonify(result)
if __name__ == '__main__':
    app.run()