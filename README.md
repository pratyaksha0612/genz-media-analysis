# Gen Z Word Processing & Sentiment Analysis Project

This project focuses on collecting Gen Z–related textual data from online news sources and preparing it for word processing and sentiment analysis, with a specific focus on temporal trends around major socio-political events.

---

## Project Status
**Current stage:**  
Web scraping, cleaning, and linguistic preprocessing completed.  
The project is now prepared for sentiment analysis using a CNN–LSTM model.

---

## Overview
The objective of this project is to study how **Generation Z** is represented in online news media and how sentiment toward Gen Z–related issues changes over time.

At the current stage, the project includes:
- Large-scale news data collection
- Data cleaning and deduplication
- Linguistic preprocessing
- Preparation for deep learning–based sentiment analysis

Further analysis will focus on sentiment trends **before, during, and after** significant events, as guided by the project supervisor.

---

## Data Collection
- News data is collected using **Google News RSS feeds**
- Broad queries related to Gen Z, youth, activism, and socio-political issues are used to ensure sufficient coverage
- Article titles and descriptions are extracted
- Each sentence is stored along with:
  - source link
  - RSS publication date

This ensures the dataset supports **temporal analysis**.

---

## Data Cleaning & Preprocessing
The collected data undergoes the following steps:
- Removal of HTML tags and noise
- Sentence-level extraction
- Deduplication to remove repeated or near-duplicate content
- Text normalization and lemmatization
- Preservation of publication dates for time-based analysis

The cleaned and preprocessed data is stored in structured CSV files.

---

## Project Structure

<pre>
WordProcessingProject/
│
├── data/
│   ├── raw/
│   │   └── genz_sentences.csv
│   │
│   └── processed/
│       ├── genz_sentences_cleaned.csv
│       └── genz_sentences_processed.csv
│
├── scripts/
│   ├── collect_data.py
│   └── clean_data.py
│
├── src/
│   └── word_preprocessing.py
│
├── archive/
│   ├── word_processing.py
│   ├── build_vocab.py
│   └── tokens_to_sequences.py
│
├── docs/
│   └── PROJECT_DETAILS.md
│
├── requirements.txt
├── README.md
└── .gitignore
</pre>

---

## Pipeline Note
Earlier scripts implementing a **classical NLP pipeline** (manual tokenization, vocabulary construction, and sequence generation) have been archived.  
The current phase uses a **CNN–LSTM–based sentiment analysis approach**, where tokenization and sequence handling are managed internally by the deep learning framework.

---

## Technologies Used
- Python  
- Requests  
- BeautifulSoup  
- Pandas  
- NLTK  
- Regular Expressions  

---

## Next Steps
- Train a CNN–LSTM model for sentiment classification using a labeled dataset
- Apply the trained model to the collected news data
- Analyze sentiment trends over time using publication dates

---

## Notes
This repository is maintained as part of a **group academic project**.  
All stages have been documented incrementally to ensure clarity, reproducibility, and alignment with academic requirements.
