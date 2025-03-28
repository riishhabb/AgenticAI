from flask import Flask, request, jsonify
from flask_cors import CORS
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("CLAUDE_API_KEY")

client = anthropic.Anthropic(api_key=api_key)


app = Flask(__name__)
CORS(app)  # ✅ Allow all origins

client = anthropic.Anthropic(api_key="API KEY")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message')

        response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    system="You are Compassion AI, a kind, non-judgmental mental health support companion who offers emotional support, encouragement, and empathetic responses. Avoid correcting grammar or spelling unless directly asked.",
    messages=[
        {"role": "user", "content": user_message}
    ]
)


        return jsonify({"response": response.content[0].text})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"response": "Sorry, something went wrong."}), 500

if __name__ == '__main__':
    app.run(debug=True)	
