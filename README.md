# Cross-lingual-Sentiment-Analysis-for-Indian-E-commerce-Reviews
# Overview
This project explores sentiment analysis across Indian languages using cross-lingual NLP models.
In the Indian e-commerce ecosystem, user reviews are often written in Hindi, Tamil, Telugu, Bengali, Marathi, and code-mixed Hinglish, which are not well supported by English-centric sentiment systems.
The objective of this work is to understand how pretrained multilingual transformers behave on such data and how uncertainty can be handled in a practical, research-oriented manner.
# Problem-Statement
- Indian e-commerce platforms receive a large number of user reviews written in multiple Indian languages and code-mixed forms such as Hinglish.
- Most existing sentiment analysis systems are English-centric and tend to classify opinions only as positive or negative, ignoring neutral or ambiguous feedback.
- As a result, a significant portion of Indian customer sentiment is either misclassified or not properly utilized.
# Motivation
From manual inspection of e-commerce platforms, a large fraction of reviews:
- Are written in non-English languages
- Contain mixed scripts or informal expressions
- Express weak or ambiguous sentiment rather than strong polarity
- Most existing sentiment systems:
- Collapse these cases into positive or negative labels
- Fail to model uncertainty explicitly
This project aims to study and address these issues using cross-lingual representations.
# Dataset and Statistics
- Dataset: Amazon Multilingual Reviews (HuggingFace)
- Domain: E-commerce
- Languages: English + multiple Indian languages
- Sample Size Used: ~1,000 reviews per language (for analysis and testing)

# Sentiment Label Distribution (approx.)

After mapping star ratings to sentiment labels:
- Positive: ~55–60%
- Neutral: ~15–20%
- Negative: ~20–25%

# Model
- Architecture: XLM-RoBERTa (multilingual transformer)
- Task: Sequence-level sentiment classification
- Labels: Positive / Neutral / Negative
- Training: No language-specific fine-tuning (zero-shot cross-lingual setup)
The model is used as-is to focus on cross-lingual generalization rather than task-specific optimization.

# Methodology
- Lightweight preprocessing
Minimal cleaning is applied to avoid removing language-specific cues.

- Cross-lingual encoding
Reviews are encoded using shared multilingual representations.

- Sentiment inference
Softmax probabilities are computed for each sentiment class.

- Confidence-based calibration
Predictions with low confidence are mapped to Neutral, instead of forcing polarity.

# Quantitative Observations
From empirical testing on multilingual and code-mixed inputs:

-Strongly polar reviews typically produce confidence scores > 0.70
- Ambiguous or mixed-opinion reviews often fall below 0.55 confidence
- Without calibration, neutral sentiment is frequently misclassified as positive or negative
- Confidence-based handling improves interpretability, especially for Indian code-mixed text

# Qualitative Analysis
Examples such as:
- “Product theek hai, price thoda zyada laga”
- “Quality achhi hai but delivery disappoint kar gayi”

show that:

- Human perception is often neutral or mixed
- Model confidence reflects this ambiguity
Explicit uncertainty handling aligns model output closer to human judgment

# Limitations
 No supervised fine-tuning on Indian-language sentiment data

- Sarcasm and implicit sentiment remain challenging

- Neutral detection relies on a heuristic threshold
These limitations are documented intentionally to maintain research transparency.

# Future Work
- More principled uncertainty modeling (entropy, margin-based methods)
- Aspect-level sentiment analysis (price, delivery, quality)
- Study of linguistic patterns in Hinglish and other code-mixed forms

# Why this matters for Multilingual NLP

This project demonstrates:
- Practical cross-lingual transfer learning

- Handling of low-resource and mixed-language text

- Explicit modeling of uncertainty

- A research-first system design mindset

It serves as a foundation for deeper multilingual NLP research rather than a finished application.



This imbalance highlights why neutral sentiment is often under-predicted by pretrained models.

