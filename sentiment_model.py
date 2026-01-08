import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_NAME = "cardiffnlp/twitter-xlm-roberta-base-sentiment"

class SentimentModel:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
        self.labels = ["Negative", "Neutral", "Positive"]

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)

        with torch.no_grad():
            logits = self.model(**inputs).logits

        probs = torch.softmax(logits, dim=1)[0]
        sentiment = self.labels[int(torch.argmax(probs))]
        confidence = float(torch.max(probs))

        return sentiment, round(confidence, 3)
