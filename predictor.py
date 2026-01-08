from modeling.sentiment_model import SentimentModel
from preprocessing.text_cleaner import clean_text

_model = SentimentModel()

def analyze(review: str):
    clean_review = clean_text(review)
    return _model.predict(clean_review)
