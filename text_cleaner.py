import re
import emoji

def clean_text(text: str) -> str:
    text = emoji.demojize(text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\u0900-\u097F\s]", "", text)
    return text.strip()
