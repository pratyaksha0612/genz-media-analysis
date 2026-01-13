# Gen Z News Text Dataset – Word Processing Project

## Project Overview

This project focuses on **collecting, cleaning, and preparing textual data related to Generation Z (Gen Z)** from online news sources for further **word processing and NLP tasks**.

The dataset is built using Google News RSS feeds and is structured to support tasks such as:

* Text preprocessing
* Tokenization
* Frequency analysis
* Sentiment analysis
* NLP-based word processing experiments

The project follows a **clean data pipeline approach**, separating raw data collection from data cleaning and preprocessing.

---

## Project Structure

```
WORDPROCESSINGPROJECT/
│
├── data/
│   ├── raw/
│   │   └── genz_sentences.csv
│   └── processed/
│       └── genz_sentences_cleaned.csv
│
├── scripts/
│   ├── collect_data.py
│   └── clean_data.py
│
├── requirements.txt
└── README.md
```

---

## Data Collection (`collect_data.py`)

* Fetches news articles using **Google News RSS feeds**
* Queries include multiple Gen Z–related topics such as lifestyle, work culture, psychology, and technology
* Extracts sentences from article titles and descriptions
* Filters sentences with **at least 6 words**
* Normalizes text to remove:

  * HTML tags
  * URLs
  * Extra whitespace
  * Unicode inconsistencies
* Removes duplicate sentences using normalized text comparison

**Output:**

```
data/raw/genz_sentences.csv
```

---

## Data Cleaning (`clean_data.py`)

* Takes raw sentences as input
* Further cleans text for word processing readiness
* Ensures consistency and readability of sentences
* Removes remaining noise and formatting issues

**Output:**

```
data/processed/genz_sentences_cleaned.csv
```

---

## Dataset Description

### `genz_sentences.csv` (Raw)

* Contains unique Gen Z–related sentences
* Directly extracted from news sources
* Includes source URLs for traceability

### `genz_sentences_cleaned.csv` (Processed)

* Cleaned and standardized version of raw data
* Ready for NLP and word processing tasks

**CSV Columns:**

* `Sentence`
* `Source`

---

## Installation & Setup

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run data collection:

```bash
python scripts/collect_data.py
```

4. Run data cleaning:

```bash
python scripts/clean_data.py
```

---

## Technologies Used

* Python 3
* Requests
* BeautifulSoup
* Regular Expressions
* CSV handling

---

## Use Cases

* Word processing assignments
* NLP preprocessing pipelines
* Linguistic analysis of Gen Z discourse
* Academic research projects

---

## Notes

* Data is collected from publicly available RSS feeds
* Project is intended for **educational and research purposes only**

---

## Future Scope

* Tokenization and lemmatization
* Sentiment analysis
* Topic modeling
* Visualization of word frequencies

---
