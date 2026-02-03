# Project Details

## Purpose of the Project
This project aims to build a structured textual dataset related to **Generation Z** by collecting news content from online sources and preparing it for advanced word processing and sentiment analysis.

The primary focus so far has been on designing a **reliable and reproducible data pipeline** that ensures data quality before applying any analytical or modeling techniques.

---

## Data Source and Collection Method
The data is collected using **Google News RSS feeds**, which provide structured access to news headlines and short descriptions from multiple publishers. RSS feeds were chosen because they:
- offer regularly updated content
- reduce the need for full web-page scraping
- ensure a consistent structure across sources

A broad set of Gen Z– and youth-related queries was used to capture diverse perspectives across social, cultural, and socio-political contexts. Each entry includes the RSS publication date to support time-based analysis.

---

## Text Extraction Strategy
From each RSS feed entry:
- article titles and descriptions are extracted
- text is treated as unstructured data
- content is split at the sentence level to improve granularity

Sentence-level extraction enables finer control during cleaning and is better suited for linguistic and sentiment-based analysis.

---

## Data Cleaning and Normalization
The collected text undergoes multiple preprocessing steps to improve quality and consistency:
- removal of HTML tags and embedded links
- normalization of punctuation and spacing
- lowercasing of text
- handling of encoding inconsistencies

These steps ensure that superficial formatting differences do not affect downstream processing.

---

## Deduplication Approach
Duplicate and near-duplicate sentences can occur due to:
- syndicated news content
- minor punctuation or formatting variations across sources

Deduplication is handled by normalizing sentences before comparison, ensuring that repeated content does not bias analysis or modeling results.

---

## Linguistic Preprocessing
After cleaning, linguistic preprocessing is applied to prepare the text for modeling:
- stopwords are removed to reduce noise
- words are lemmatized to their base forms
- sentences are converted into normalized textual representations

This step reduces vocabulary size and improves semantic consistency, which is especially important for deep learning–based models.

---

## Pipeline Evolution
The project initially explored a **classical NLP pipeline**, including manual tokenization, vocabulary construction, and sequence generation. As the project scope evolved toward **CNN–LSTM–based sentiment analysis**, these steps were replaced by an end-to-end deep learning pipeline.

Tokenization and sequence generation are now handled internally by the neural network framework. The earlier scripts have been archived for reference and documentation of the project’s evolution.

---

## Preparation for Sentiment Analysis
At the current stage:
- the dataset is cleaned, deduplicated, and linguistically preprocessed
- publication dates are preserved for temporal analysis
- the data is ready to be passed directly into a CNN–LSTM sentiment classification model

This setup supports analysis of sentiment trends **before, during, and after** significant events.

---

## Current Status
The web scraping and preprocessing pipeline has been completed successfully.  
The dataset is structured and ready for model training and sentiment-based analysis.

---

## Design Considerations
The project follows a modular design:
- data collection, cleaning, and preprocessing are handled in separate scripts
- each stage produces a clearly defined output
- the pipeline is easy to audit, reproduce, and extend

This structure supports both academic evaluation and future experimentation.

---

## Scope for Next Steps
The next phase of the project will involve:
- training a CNN–LSTM model using a labeled sentiment dataset
- applying the trained model to the collected news data
- analyzing sentiment trends over time using publication dates

Further refinements will be carried out based on project review and guidance.
