# Project Details

## Overview
This project builds a **clean, sentence-level text dataset** related to *Generation Z* using online news content. The processed data is designed for **word processing and NLP-based analysis**, such as text analysis, topic modeling, and sentiment studies.

---

## What Are RSS Feeds?
**RSS (Really Simple Syndication)** feeds are structured XML files used by news websites to publish updated content like headlines and summaries. They allow automated and reliable data collection without scraping full web pages.

---

## Why Google News RSS?
Google News aggregates articles from multiple verified publishers. Using its RSS feeds ensures:
- Diverse and up-to-date sources
- Reduced publisher bias
- Consistent data structure

---

## Data Collection Process
- Multiple Gen Z–related queries are defined (lifestyle, trends, work culture, psychology, technology).
- For each query, a Google News RSS feed is fetched.
- Article titles, descriptions, and source links are extracted.

---

## Text Processing
- Text is split into individual sentences.
- Short or low-information sentences are discarded.
- HTML tags, URLs, and extra whitespace are removed.
- Unicode characters and punctuation are normalized.

---

## Deduplication
To avoid repetition across articles and sources:
- Each sentence is normalized (case, punctuation, spacing).
- Only unique sentences are retained.
- Original readable text is preserved in the final dataset.

---

## Dataset Output
The final dataset is stored as a CSV file with:
- **Sentence** – cleaned Gen Z–related text
- **Source** – corresponding article link

Files are organized into:
- `data/raw/` – unprocessed data
- `data/processed/` – cleaned dataset

---

## Intended Use
This dataset is suitable for:
- Word processing experiments
- NLP analysis and modeling
- Media and linguistic analysis of Gen Z narratives

---

## Design Approach
The project emphasizes:
- Data quality over volume
- Clear preprocessing steps
- Reproducibility and documentation
