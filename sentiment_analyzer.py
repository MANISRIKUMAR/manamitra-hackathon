import os
from google.cloud import language_v1

class SentimentAnalyzer:
    def __init__(self):
        self.credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        if not self.credentials_path:
            raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set.")
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credentials_path
        self.client = language_v1.LanguageServiceClient()

    def analyze(self, text):
        document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
        sentiment = self.client.analyze_sentiment(request={"document": document}).document_sentiment
        score = sentiment.score

        if score > 0.2:
            return {"emotion": "happy"}
        elif score < -0.2:
            return {"emotion": "sad"}
        else:
            return {"emotion": "neutral"}
