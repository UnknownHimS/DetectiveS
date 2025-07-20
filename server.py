# server.py
from flask import Flask, request, jsonify
import openai
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow frontend to access this server

openai.api_key = os.getenv("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")  # store your key in Render environment

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
