# app.py
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from emotional_responder import EmotionalResponder
from sentiment_analyzer import SentimentAnalyzer
import re

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Use a secure key in production
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

response_agent = EmotionalResponder()
analyzer = SentimentAnalyzer()

SENSITIVE_KEYWORDS = ["suicide", "depressed", "kill myself", "end my life"]

@app.route('/')
def index():
    history = session.get("chat", [])
    return render_template('index.html', history=history)

@app.route('/respond', methods=['POST'])
def respond():
    data = request.json
    user_input = data.get("message", "")

    if "chat" not in session:
        session["chat"] = []
    if "name" not in session:
        session["name"] = None

    name_match = re.search(r"my name is ([A-Za-z]+)", user_input, re.IGNORECASE)
    if name_match:
        session["name"] = name_match.group(1)
        reply = f"Hi {session['name'].title()}, it's nice to meet you!"
    elif "what is my name" in user_input.lower():
        reply = f"Your name is {session['name'].title()}! 😊" if session["name"] else "You haven't told me your name yet!"
    elif any(keyword in user_input.lower() for keyword in SENSITIVE_KEYWORDS):
        reply = response_agent.handle_sensitive_topic()
    else:
        emotion = analyzer.analyze(user_input)["emotion"]
        reply = response_agent.generate_response(emotion, user_input)

    session["chat"].append({"you": user_input, "bot": reply})
    session.modified = True

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
