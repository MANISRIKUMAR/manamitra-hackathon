# ManaMitra – A Multi-Agent AI Companion for Emotional Support

## 💡 Project Overview

**ManaMitra** is a web-based emotional support assistant that leverages multiple AI agents to provide empathetic, human-like conversations in both **text** and **voice** modes. It combines the power of **Google Cloud Natural Language API**, **Gemini (Vertex AI)**, and **speech recognition** to assist users emotionally, especially during tough moments.

## 🎯 Features

* 🤖 **Multi-Agent System**: Includes a sentiment analyzer and a Gemini-powered emotional response generator.
* 🗣️ **Text and Voice Chat**: Interact using typed messages or your voice.
* 💬 **Empathetic Responses**: Detects emotion and responds accordingly.
* ☁️ **Powered by Google Cloud**: Uses Vertex AI and Cloud NLP APIs.
* 🧠 **Suicidal Thought Handling**: Detects sensitive words and gives caring responses.

## 🏗️ Tech Stack

| Component | Technology                        |
| --------- | --------------------------------- |
| Frontend  | HTML, CSS, JavaScript             |
| Backend   | Python (Flask)                    |
| AI Model  | Google Gemini (via Vertex AI)     |
| Sentiment | Google Cloud Natural Language API |
| Speech    | Web Speech API (browser-based)    |

## 🔄 Architecture

```
User ↔️ Web UI (text/voice)
       ↘️                           ↙️
  SpeechRecognition API    ➡️ Flask Backend ⬅️
                             |         |
                SentimentAnalyzer   EmotionalResponder
                    (NLP API)          (Gemini)
                             ⬇️
                       Empathetic Reply
```

## 🚀 How to Run Locally

1. Clone this repo
2. Set your `GOOGLE_APPLICATION_CREDENTIALS` in environment
3. Install dependencies:

```bash
pip install flask google-cloud-language vertexai
```

4. Run the app:

```bash
python app.py
```

5. Open in browser: `http://127.0.0.1:5000`

## 📹 Demo Video

\[Insert YouTube link here]

## 📁 Folder Structure

```
├── app.py
├── agents/
│   ├── emotional_responder.py
│   └── sentiment_analyzer.py
├── static/
│   └── bot-audio.wav
├── templates/
│   └── index.html
├── README.md
```

## 🧠 Key Learnings

* Working with multiple AI services in sync
* Voice input integration in browser
* Deploying intelligent, supportive web agents

## 📜 License

MIT License

## 🙌 Team

Built with ❤️ by Mani Sri Kumar for the Google Cloud + Devpost Hackathon 2025.

Thankyou
