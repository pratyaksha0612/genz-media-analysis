# Gen Z Word Processing Project

This project focuses on collecting Gen Z–related textual data from online news sources and preparing it for word processing and further text analysis.

## Project Status
**Current stage:** Web scraping completed and data prepared for word processing.

---

## Overview
The objective of this project is to study how Generation Z is represented in online news media.  
At this stage, the work focuses on:
- Collecting relevant textual data
- Cleaning and structuring the data
- Preparing it for word processing tasks

Further word processing and analysis will be carried out based on guidance from the project supervisor.

---

## Data Collection
- News data is collected using **Google News RSS feeds**
- Multiple Gen Z–related queries are used to ensure coverage across topics such as lifestyle, work culture, psychology, and technology
- Article titles and descriptions are extracted as text data

---

## Data Cleaning & Preparation
The collected data undergoes the following steps:
- Removal of HTML tags and noise
- Sentence-level extraction
- Deduplication to remove repeated content
- Text normalization and preprocessing
- Tokenization for word-level processing

The processed data is stored in structured CSV files for further analysis.

---

## Project Structure
WordProcessingProject/
│
├── data/
│ ├── raw/ # Collected raw data
│ └── processed/ # Cleaned and processed datasets
│
├── scripts/
│ ├── collect_data.py
│ └── clean_data.py
│
├── src/
│ ├── word_preprocessing.py
│ ├── word_processing.py
│ ├── build_vocab.py
│ └── tokens_to_sequences.py
│
├── docs/
│ └── PROJECT_DETAILS.md
│
├── requirements.txt
└── README.md

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
- Proceed with word processing and analysis as per supervisor’s instructions
- Explore word frequency, patterns, or other linguistic insights if required

---

## Notes
This repository is maintained as part of a **group academic project**.  
All progress has been documented incrementally to ensure clarity and reproducibility.
