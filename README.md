# GenZ Media Sentiment Analysis  
### A Comparative Study of Institutional Media vs Public Sentiment During the Nepal Protest


## 📌 Project Overview

This project performs a **temporal sentiment analysis** on Generation Z–related discourse surrounding the Nepal protest.  

The study analyzes sentiment across three time phases:

- **Before the protest**
- **During the protest**
- **After the protest**

The project compares:

1. **News headlines (Google RSS feeds)**
2. **YouTube public comments**
3. **VADER (Rule-based NLP)**
4. **CNN + LSTM (Deep Learning Model)**

The goal is to understand how institutional media tone differs from public sentiment and how traditional NLP compares with deep learning approaches.

---

## 🎯 Research Objectives

- Analyze sentiment trends across protest phases.
- Compare institutional media vs public discourse.
- Compare lexicon-based NLP with deep learning.
- Evaluate sentiment shifts across time.

---

## 📂 Project Structure

.
│   .gitignore
│   README.md
│   requirements.txt
│
├───docs
│       PROJECT_DETAILS.md
│
├───RSS_ANALYSIS
│   ├───data
│   │   ├───final
│   │   │       genz_sentiment_results.csv
│   │   │
│   │   ├───processed
│   │   │       genz_sentences_cleaned.csv
│   │   │       genz_sentences_processed.csv
│   │   │
│   │   └───raw
│   │           genz_sentences.csv
│   │
│   ├───notebooks
│   │       cnn_lstm_rss.ipynb
│   │
│   ├───scripts
│   │       clean_data.py
│   │       collect_data.py
│   │
│   └───src
│           word_preprocessing.py
│
├───YT_ANALYSIS
│   ├───models
│   │       cnn_lstm_imdb_sentiment_model.h5
│   │
│   ├───notebooks
│   │       cnn_lstm_analysis.ipynb
│   │       vader_analysis.ipynb
│   │
│   ├───processed
│   │       cleaned_data.csv
│   │       sentiment_labeled_data.csv
│   │
│   ├───raw
│   │       youtube_nepal_genz_dataset.csv
│   │
│   └───scripts
│           generate_sentiment_labels.py
│           preprocess.py
│           sentiment_check.py
│           yt_scrapper.py
```

---

## 🔎 Data Sources

### 1️⃣ RSS Headlines
- Collected using Google RSS feeds
- Institutional news perspective
- Structured into raw → processed → final stages

### 2️⃣ YouTube Comments
- Scraped from protest-related videos
- Higher emotional variance than headlines
- Used for both VADER and CNN+LSTM analysis

---

## ⚙️ Methodology

### A. Data Collection

- RSS headlines collected using `collect_data.py`
- YouTube comments scraped using `yt_scrapper.py`


### B. Data Preprocessing

Steps applied:
- Lowercasing
- URL removal
- Punctuation removal
- Stopword removal
- Tokenization
- Sequence padding (for deep learning)

Files:
- `clean_data.py`
- `preprocess.py`
- `word_preprocessing.py`


### C. Sentiment Analysis Techniques

#### 1️⃣ VADER (Lexicon-Based NLP)

- Rule-based sentiment analyzer
- Generates compound score
- Classified into:
  - Positive
  - Neutral
  - Negative

Notebook:
- `vader_analysis.ipynb`

Used as baseline NLP model.

---

#### 2️⃣ CNN + LSTM (Deep Learning Model)

Hybrid architecture:

- Embedding Layer
- Convolutional Layer (feature extraction)
- MaxPooling
- LSTM Layer (context learning)
- Dense Output Layer (Softmax classification)

Model file:
- `cnn_lstm_imdb_sentiment_model.h5`

Notebooks:
- `cnn_lstm_rss.ipynb`
- `cnn_lstm_analysis.ipynb`

Purpose:
- Capture contextual sentiment patterns
- Compare performance against VADER

---

## 📊 Comparative Analysis

This project performs three levels of comparison:

### 1️⃣ Source Comparison
- RSS Headlines vs YouTube Comments

### 2️⃣ Method Comparison
- VADER vs CNN + LSTM

### 3️⃣ Temporal Comparison
- Before vs During vs After Protest

---

## 📈 Key Observations

- RSS headlines show relatively neutral sentiment distribution.
- YouTube comments exhibit higher emotional polarization.
- CNN + LSTM captures contextual sentiment shifts better than VADER.
- Institutional media tone differs from public reaction.

---

## ⚠️ Limitations

- Headlines are short and often neutral.
- CNN + LSTM model trained on general sentiment data (not protest-specific).
- API restrictions limited Twitter/Reddit data collection.
- YouTube scraping constrained by time range availability.

---

## 🚀 Future Improvements

- Train protest-specific sentiment model.
- Integrate Twitter/X data (if API access available).
- Add topic modeling.
- Include accuracy metrics and confusion matrix.
- Expand dataset diversity.

---

## 🛠 Requirements

Install dependencies:

```
pip install -r requirements.txt
```


## 🧠 Tech Stack

- Python
- Pandas
- NumPy
- NLTK
- VADER
- TensorFlow / Keras
- CNN + LSTM Architecture
- Jupyter Notebook

---

## 👩‍💻 Author

Pratyaksha Singh  
B.Tech CSE (AI & ML)  
NLP | Sentiment Analysis | Deep Learning | Media Analytics
