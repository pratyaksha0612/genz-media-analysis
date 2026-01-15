# Project Details

## Purpose of the Project
This project aims to build a structured textual dataset related to **Generation Z** by collecting news content from online sources and preparing it for word processing tasks. The focus of the work so far has been on creating a reliable and clean data pipeline that can support further textual analysis.

The intention is to first ensure high-quality data collection and preparation before proceeding to deeper word processing or analytical stages.


## Data Source and Collection Method
The data is collected using **Google News RSS feeds**, which provide structured access to news headlines and short descriptions from multiple publishers. RSS feeds were chosen because they:
- offer regularly updated content
- reduce the need for full web-page scraping
- ensure consistent data structure across sources

Multiple Gen Z–related search queries were used to collect diverse news coverage across social, cultural, and professional contexts.


## Text Extraction Strategy
From each RSS feed entry:
- article titles and descriptions are extracted
- text is treated as raw unstructured data
- content is split at the sentence level to improve granularity

Sentence-level extraction allows better control during cleaning and makes the dataset more suitable for word processing and linguistic analysis.

## Data Cleaning and Normalization
The collected text undergoes several preprocessing steps to improve quality and consistency:
- removal of HTML tags and unnecessary symbols
- normalization of punctuation and spacing
- lowercasing of text
- handling of encoding inconsistencies

These steps ensure that superficial formatting differences do not affect later processing stages.


## Deduplication Approach
Duplicate and near-duplicate sentences can occur due to:
- similar headlines published by different sources
- minor punctuation or formatting variations

Deduplication is handled during preprocessing by normalizing sentences before comparison. This ensures that repeated content does not bias later word-level analysis.


## Linguistic Preprocessing
After cleaning, linguistic preprocessing is applied to prepare the text for word processing:
- stopwords are removed to reduce noise
- words are lemmatized to bring them to their base forms
- sentences are transformed into normalized representations

This step improves consistency and reduces vocabulary size, which is important for meaningful word-level analysis.

## Tokenization and Structuring
The processed text is then tokenized:
- sentences are broken into individual word tokens
- very short or insignificant tokens are filtered out
- structured token lists are generated for each sentence

This representation bridges the gap between raw text and numerical processing.


## Preparation for Word Processing
To support future word processing tasks:
- a vocabulary mapping is created from the tokenized data
- words are converted into numerical sequences
- processed datasets are stored in a reusable format

At this stage, the data is **fully prepared** for word processing, frequency analysis, or further NLP-based exploration.



## Current Status
The web scraping and data preparation pipeline has been completed successfully.  
The dataset is cleaned, structured, and ready for the next phase of word processing, which will be carried out based on further project guidance.



## Design Considerations
The project follows a modular design:
- data collection, cleaning, and processing are handled in separate steps
- each stage produces a clear output for the next stage
- this structure improves reproducibility and ease of explanation

This approach ensures clarity both for academic evaluation and future extensions.


## Scope for Next Steps
Depending on requirements, the prepared data can be used for:
- word frequency and pattern analysis
- phrase and n-gram extraction
- thematic or sentiment-based studies

Further analysis will be determined after review of the current stage.
