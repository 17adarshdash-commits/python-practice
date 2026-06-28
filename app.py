from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
if __name__ == '__main__':
    app.run()