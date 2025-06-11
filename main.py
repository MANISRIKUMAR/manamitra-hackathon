from flask import Flask, request, jsonify,render_template
from agents.emotional_responder import EmotionalResponder
from agents.sentiment_analyzer import SentimentAnalyzer

app = Flask(__name__)

# Initialize agents
response_agent = EmotionalResponder()
sentiment_agent = SentimentAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Analyze sentiment
    result = sentiment_agent.analyze(user_input)
    emotion = result["emotion"]

    # Generate empathetic response
    reply = response_agent.generate_response(emotion, user_input)

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)