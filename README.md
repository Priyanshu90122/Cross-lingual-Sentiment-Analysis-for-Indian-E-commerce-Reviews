# Cross-lingual Sentiment Analysis for Indian E-commerce Reviews

This project investigates zero-shot cross-lingual sentiment analysis for Indian
e-commerce reviews using pretrained multilingual transformers. Indian user-generated
content is inherently multilingual and code-mixed (e.g., Hindi, Tamil, Telugu,
Bengali, Marathi, and Hinglish), posing challenges for sentiment models trained
primarily on English data.

The objective of this work is **not to maximize accuracy**, but to analyze
cross-lingual transfer behavior, model uncertainty, and error patterns when applying
a single multilingual model across diverse Indian languages without language-specific
fine-tuning. The project is designed as a **research-oriented study**, focusing on
model behavior, calibration, and limitations rather than application-level
optimization.

---

## Problem Statement

Indian e-commerce platforms receive large volumes of reviews written in multiple
Indian languages and code-mixed forms such as Hinglish. Existing sentiment analysis
systems are largely English-centric and often collapse ambiguous feedback into
binary positive or negative labels.

This leads to:
- Poor handling of **neutral or mixed sentiment**
- Systematic misclassification of **code-mixed reviews**
- Lack of **uncertainty awareness** in predictions

This project studies these challenges through a controlled **zero-shot multilingual
evaluation**.

---

## Methodology (Research Framing)

- **Dataset**: Amazon Multilingual Reviews (HuggingFace)
- **Languages**: English, Hindi, Tamil, Telugu, Bengali, Marathi + synthetic Hinglish
- **Label Mapping**:
  - 1–2 stars → Negative
  - 3 stars → Neutral
  - 4–5 stars → Positive

- **Model**: XLM-RoBERTa (pretrained multilingual transformer)
- **Setup**: Zero-shot inference (no supervised fine-tuning)
- **Inference**: Softmax probabilities over sentiment classes
- **Uncertainty Handling**: Confidence-based calibration, mapping low-confidence
  predictions to Neutral

This setup isolates **cross-lingual generalization effects** from task-specific
fine-tuning.

---

## Key Observations

- Strongly polar reviews typically produce confidence scores **> 0.70**
- Ambiguous or mixed-opinion reviews often fall below **0.55 confidence**
- Without calibration, neutral sentiment is frequently misclassified
- Confidence-based handling improves interpretability for Indian and code-mixed text

---

## Limitations

- No supervised fine-tuning on Indian-language sentiment datasets
- Sarcasm and implicit sentiment remain challenging
- Neutral detection relies on heuristic confidence thresholds

These limitations are explicitly acknowledged to maintain **research transparency**.

---

## Why This Matters for Multilingual NLP

This project demonstrates:
- Practical **cross-lingual transfer analysis**
- Challenges of **low-resource and code-mixed text**
- Importance of **uncertainty modeling** in multilingual NLP systems

Overall, it reflects a **research-first system design** suitable for deeper
multilingual NLP studies rather than a finalized application.
