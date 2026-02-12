📰📊 Gen Z Media Sentiment Analysis

This project analyzes how Generation Z is portrayed and discussed across different media sources using Natural Language Processing and Deep Learning techniques.
The repository consists of two major analytical pipelines:
RSS News Media Analysis
YouTube Protest Discourse Analysis
The project combines:
Lexicon-based sentiment analysis (VADER)
Deep learning using CNN + LSTM
Cross-domain comparison of sentiment patterns

📂 Repository Structure
WordProcessingProject/
│
├── RSS_ANALYSIS/
├── YT_ANALYSIS/
├── doc+s/
├── README.md
└── requirements.txt

📰 1️⃣ RSS_ANALYSIS – News Media Sentiment
Objective
To analyze how Gen Z is portrayed in online news media using RSS feeds.
Pipeline
RSS feed collection
Text preprocessing
Sentence-level sentiment extraction
CNN + LSTM model training on RSS data
Sentiment result aggregation

Key Files
RSS_ANALYSIS/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
│
├── notebooks/
│   └── cnn_lstm_rss.ipynb
│
├── scripts/
│   ├── collect_data.py
│   └── clean_data.py
│
└── src/
    └── word_preprocessing.py

Outcome
The RSS pipeline provides sentiment trends in traditional news coverage related to Gen Z.

📺 2️⃣ YT_ANALYSIS – YouTube Protest Sentiment
Objective
To analyze how public sentiment toward Gen Z evolved:
Before the Nepal protest (8–13 September 2025)
During the protest
After the protest
Data Collection
Source: YouTube comments
Time Window:
2 months before protest
Protest duration
2 months after protest
Dataset: ~1100 cleaned comments

Methods Used
A. Lexicon-Based Sentiment (VADER)

Classifies: Positive / Neutral / Negative
Optimized for social media
Used to compute 3-class sentiment distribution

B. Deep Learning Sentiment (CNN + LSTM)

Architecture:
Embedding → Conv1D → MaxPooling → LSTM → Dense → Sigmoid

Training Strategy:
Model trained on IMDB dataset (~25,000 labeled reviews)
Achieved ~85% validation accuracy
Applied to Gen Z dataset for binary sentiment prediction

This ensures:
Robust deep learning sentiment modeling
Cross-domain validation

Key Findings
RSS Media:
News sentiment trends show structured portrayal patterns.
YouTube Protest Data:
Pre-protest phase exhibited highest negative sentiment.
During and post-protest phases showed increased positivity.
Both VADER and CNN + LSTM indicate measurable sentiment shifts.

🧠 Research Contribution
This project demonstrates:
Cross-platform sentiment comparison (News vs YouTube)
Lexicon-based vs Deep Learning approaches
Domain transfer learning for sentiment classification
Temporal sentiment evolution analysis

🛠 Technologies Used
Python
Pandas
NLTK (VADER)
TensorFlow / Keras
CNN + LSTM
Matplotlib / Seaborn

📌 Conclusion
The combined use of traditional NLP and deep learning methods reveals dynamic sentiment shifts in media discourse about Generation Z across platforms and time periods.