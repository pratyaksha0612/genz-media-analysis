# PROJECT DETAILS  
## GenZ Media Sentiment Analysis: Temporal Study of Nepal Protest

---

# 1. INTRODUCTION

This project performs a structured sentiment analysis study on discourse related to Generation Z and the Nepal protest. The objective is to analyze how sentiment shifts across time and across platforms, and to compare traditional Natural Language Processing (NLP) methods with Deep Learning approaches.

The study is designed around three core dimensions:

1. Temporal Dimension  
   - Before Protest  
   - During Protest  
   - After Protest  

2. Source Dimension  
   - Institutional Media (RSS Headlines)  
   - Public Discourse (YouTube Comments)  

3. Methodological Dimension  
   - Rule-based NLP (VADER)  
   - Deep Learning (CNN + LSTM)

This multi-dimensional design allows comparative evaluation of sentiment behavior and modeling techniques.

---

# 2. PROBLEM STATEMENT

Media representation and public reaction often differ significantly during socio-political events. Traditional sentiment analysis tools may fail to capture contextual nuance, while deep learning models require structured preprocessing and large datasets.

This project aims to answer:

- Does institutional media maintain neutral sentiment during protests?
- Does public sentiment become more polarized during protest periods?
- Does CNN + LSTM outperform lexicon-based methods in contextual sentiment detection?
- How does sentiment shift across protest phases?

---

# 3. SYSTEM ARCHITECTURE

The project is divided into two primary pipelines:

1. RSS Analysis Pipeline  
2. YouTube Analysis Pipeline  

Each pipeline follows structured stages:

Data Collection → Data Cleaning → Preprocessing → Sentiment Analysis → Comparative Evaluation

---

# 4. RSS ANALYSIS PIPELINE

## 4.1 Data Collection

File:
```
RSS_ANALYSIS/scripts/collect_data.py
```

Process:
- Google RSS feeds were queried for protest-related keywords.
- Headlines were collected.
- Time filtering applied to segment into:
  - Before protest
  - During protest
  - After protest

Output:
```
RSS_ANALYSIS/data/raw/genz_sentences.csv
```

This dataset contains short news headlines.

---

## 4.2 Data Cleaning

File:
```
RSS_ANALYSIS/scripts/clean_data.py
```

Cleaning steps:
- Lowercasing
- Removal of URLs
- Removal of special characters
- Removal of punctuation
- Removal of extra whitespace

Output:
```
RSS_ANALYSIS/data/processed/genz_sentences_cleaned.csv
```

---

## 4.3 Text Preprocessing

File:
```
RSS_ANALYSIS/src/word_preprocessing.py
```

Steps:
- Tokenization
- Stopword removal
- Lemmatization (if applied)
- Vocabulary construction
- Sequence generation
- Padding sequences for model compatibility

Output:
```
RSS_ANALYSIS/data/processed/genz_sentences_processed.csv
```

---

## 4.4 CNN + LSTM on RSS

Notebook:
```
RSS_ANALYSIS/notebooks/cnn_lstm_rss.ipynb
```

Purpose:
Apply deep learning model to RSS headlines.

Limitation:
Headlines are short and generally neutral, leading to limited emotional diversity.

Final Output:
```
RSS_ANALYSIS/data/final/genz_sentiment_results.csv
```

---

# 5. YOUTUBE ANALYSIS PIPELINE

## 5.1 Data Collection

File:
```
YT_ANALYSIS/scripts/yt_scrapper.py
```

Process:
- Identified protest-related YouTube videos.
- Scraped comments within relevant date ranges.
- Filtered for GenZ-related keywords if required.

Output:
```
YT_ANALYSIS/raw/youtube_nepal_genz_dataset.csv
```

Unlike headlines, comments contain informal language, slang, and emotional polarity.

---

## 5.2 Preprocessing

File:
```
YT_ANALYSIS/scripts/preprocess.py
```

Steps:
- Lowercasing
- URL removal
- Emoji removal (if implemented)
- Punctuation removal
- Tokenization
- Stopword removal
- Sequence padding

Output:
```
YT_ANALYSIS/processed/cleaned_data.csv
```

---

## 5.3 Sentiment Label Generation (For DL Model)

File:
```
YT_ANALYSIS/scripts/generate_sentiment_labels.py
```

Purpose:
- Generate labeled sentiment data
- Prepare dataset for CNN+LSTM input

Output:
```
YT_ANALYSIS/processed/sentiment_labeled_data.csv
```

---

# 6. SENTIMENT ANALYSIS METHODS

## 6.1 VADER (Rule-Based NLP)

Notebook:
```
YT_ANALYSIS/notebooks/vader_analysis.ipynb
```

VADER Characteristics:
- Lexicon-based
- Uses predefined sentiment dictionary
- Generates compound polarity score

Classification:
- Compound > threshold → Positive
- Compound < negative threshold → Negative
- Otherwise → Neutral

Advantages:
- Fast
- No training required

Limitations:
- Cannot understand contextual sarcasm
- Limited deep contextual learning

---

## 6.2 CNN + LSTM Model

Model file:
```
YT_ANALYSIS/models/cnn_lstm_imdb_sentiment_model.h5
```

Notebook:
```
YT_ANALYSIS/notebooks/cnn_lstm_analysis.ipynb
```

Architecture Explanation:

1. Embedding Layer  
   Converts words into dense vector representations.

2. Convolutional Layer (CNN)  
   Extracts local n-gram features.

3. MaxPooling Layer  
   Reduces dimensionality and retains strongest features.

4. LSTM Layer  
   Captures long-term sequential dependencies.

5. Dense Output Layer (Softmax)  
   Produces probability distribution over sentiment classes.

Why CNN + LSTM?
- CNN captures local textual features.
- LSTM captures sequential context.
- Hybrid model improves contextual sentiment detection.

---

# 7. COMPARATIVE FRAMEWORK

The project performs three structured comparisons:

## 7.1 Temporal Comparison
Sentiment distribution:
- Before Protest
- During Protest
- After Protest

Observation goal:
Identify sentiment shift trends.

---

## 7.2 Source Comparison
- RSS Headlines (Institutional Media)
- YouTube Comments (Public Sentiment)

Objective:
Compare neutrality vs emotional polarization.

---

## 7.3 Method Comparison
- VADER
- CNN + LSTM

Objective:
Evaluate:
- Contextual sensitivity
- Emotional polarity detection
- Distribution differences

---

# 8. KEY FINDINGS

1. RSS headlines largely neutral.
2. YouTube comments highly polarized.
3. Public discourse more emotionally reactive.
4. CNN + LSTM captures contextual shifts better than VADER.
5. Institutional media tone differs significantly from grassroots reaction.

---

# 9. LIMITATIONS

- RSS headlines lack emotional depth.
- Deep learning model trained on general sentiment dataset (not protest-specific).
- Twitter and Reddit APIs restricted data access.
- YouTube scraping limited by availability of comments.

---

# 10. TECH STACK

- Python
- Pandas
- NumPy
- NLTK
- VADER
- TensorFlow
- Keras
- CNN + LSTM Architecture
- Jupyter Notebook

---

# 11. FUTURE IMPROVEMENTS

- Train protest-specific sentiment model.
- Incorporate transformer-based models (e.g., BERT).
- Add topic modeling.
- Include performance metrics (Accuracy, F1, Confusion Matrix).
- Increase dataset size and diversity.

---

# 12. CONCLUSION

This project demonstrates that:

- Institutional media tone remains comparatively neutral.
- Public discourse becomes emotionally polarized during socio-political unrest.
- Deep learning methods outperform lexicon-based approaches in contextual understanding.
- Multi-source, multi-method analysis provides stronger research insights than single-source studies.

The study serves as a comparative framework for media analytics and sentiment modeling across time and platforms.

---

