Project Details: Gen Z Media Analysis
1. Project Objective

This project focuses on building a clean, sentence-level textual dataset related to Generation Z by collecting news content from multiple online sources and preparing it for word processing and NLP-based analysis.

The primary objective is to:

Gather diverse, real-world textual data related to Gen Z

Clean and normalize the text

Remove duplicates and noise

Produce a structured dataset suitable for downstream NLP tasks such as:

Text analysis

Word frequency analysis

Topic modeling

Sentiment analysis

Linguistic pattern discovery

2. What Are RSS Feeds?

RSS (Really Simple Syndication) feeds are standardized XML-based formats used by news websites to publish frequently updated content such as:

Headlines

Short descriptions

Source links

RSS feeds allow automated programs to fetch the latest content without scraping entire web pages, making them:

Lightweight

Reliable

Legally safer than full-page scraping

3. Why Google News RSS?

Google News aggregates articles from a wide range of verified news publishers across:

Countries

Media houses

Political and cultural perspectives

Using Google News RSS feeds ensures:

High source diversity

Current and relevant content

Reduced bias from a single publisher

Consistent XML structure for parsing

Each query returns multiple articles related to Gen Z from different sources.

4. Data Collection Strategy

The data collection process follows these steps:

Multiple Gen Z–related search queries are defined (e.g., lifestyle, work culture, psychology, technology).

For each query:

A Google News RSS feed URL is generated

The feed is fetched using HTTP requests

From each RSS item:

Article title

Short description

Source link
are extracted.

This ensures coverage across social, cultural, psychological, and technological dimensions of Gen Z.

5. Sentence-Level Extraction

Rather than storing full titles or descriptions as-is, the text is:

Split into individual sentences

Filtered to keep sentences with meaningful length (minimum word count)

Why sentence-level data?

More suitable for NLP tasks

Reduces noise from long, mixed-topic paragraphs

Enables fine-grained linguistic and semantic analysis

6. Text Cleaning and Normalization

Several cleaning steps are applied to ensure data quality:

HTML Cleaning

Removes HTML tags

Converts encoded characters into readable text

Noise Removal

Removes URLs

Normalizes extra whitespace

Cleans punctuation artifacts

Unicode Normalization

Handles smart quotes, dashes, and encoding inconsistencies

Ensures uniform text representation

7. Deduplication Logic

Duplicate sentences can appear across:

Multiple articles

Different publishers

Slight textual variations

To handle this, a normalized key is generated for each sentence by:

Converting text to lowercase

Removing quotes

Normalizing punctuation and spacing

Trimming trailing symbols

Only unique normalized sentences are retained, while the original readable sentence is preserved in the final dataset.

8. Dataset Structure
Raw Data

Stored in data/raw/

Contains collected but unprocessed text

Processed Data

Stored in data/processed/

Contains:

Cleaned

Sentence-level

Deduplicated text

Source URLs

Final output format:
CSV with two columns

Sentence

Source

9. Intended Use of the Dataset

The cleaned dataset is designed specifically for:

Word processing experiments

NLP model training or evaluation

Linguistic and behavioral analysis of Gen Z representation in media

Academic coursework and research projects

The pipeline ensures reproducibility and clarity, making it suitable for further extensions.

10. Project Design Philosophy

This project prioritizes:

Clean data over raw volume

Explainable preprocessing steps

Modular and reproducible scripts

Academic clarity and documentation

It serves as a foundational layer for more advanced NLP or machine learning workflows.