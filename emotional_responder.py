import os
from vertexai.preview.generative_models import GenerativeModel
import vertexai

class EmotionalResponder:
    def __init__(self):
        self.credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not self.credentials_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set.")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path

        self.project_id = "manamitra-hackathon"
        self.location = "us-central1"
        vertexai.init(project=self.project_id, location=self.location)
        self.model = GenerativeModel("gemini-2.0-flash")

    def generate_response(self, emotion, user_input=None):
        prompt_map = {
            "sad": "The user is feeling down. Respond with empathy:",
            "happy": "The user is joyful. Respond warmly:",
            "neutral": "The user seems neutral. Respond gently:"
        }
        prompt = prompt_map.get(emotion, "Respond naturally:")
        try:
            response = self.model.generate_content(
                prompt + f"\nUser: {user_input}",
                generation_config={
                    "max_output_tokens": 60,
                    "temperature": 0.7
                }
            )
            return response.text.strip()
        except Exception as e:
            print(f"Error generating response: {e}")
            return "I'm here for you. Let me know how I can help."

    def handle_sensitive_topic(self):
        return (
            "I'm really sorry you're feeling this way. You're not alone, and your feelings are valid. "
            "It might help to talk to a friend, family member, or mental health professional. "
            "Would you like me to suggest some support resources? 💛"
        )
