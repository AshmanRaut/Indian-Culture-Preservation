import flask
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

genai.configure(api_key="AIzaSyDXR_-3lFrHUJDjZkhviARx5yuT761G7tM")
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)
CORS(app) 

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')

        response = model.generate_content(user_message)
        
        return jsonify({
            'response': response.text
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)