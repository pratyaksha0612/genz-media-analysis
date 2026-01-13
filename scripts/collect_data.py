import requests
from bs4 import BeautifulSoup
import csv
import re
import time
import unicodedata
import os

queries = [
    "Gen Z",
    "Generation Z",
    "Gen Z lifestyle",
    "Gen Z trends",
    "Gen Z work culture",
    "Gen Z report",
    "Gen Z analysis",
    "Gen Z India",
    "Gen Z behavior",
    "Gen Z news",
    "Gen Z technology",
    "Gen Z psychology",
    "Gen Z social media"
]

all_sentences = []

def clean_html(text):
    text = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\.\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def normalize_for_dedup(text):
    # Unicode normalization
    text = unicodedata.normalize("NFKD", text)

    # Normalize dashes
    text = re.sub(r"[–—−]", "-", text)

    # Remove quotes (single, double, smart quotes)
    text = re.sub(r"[\"'‘’“”]", "", text)

    # Normalize punctuation spacing
    text = re.sub(r"\s*-\s*", " - ", text)
    text = re.sub(r"\s+", " ", text)

    # Remove trailing punctuation
    text = text.strip(" .,-:")

    return text.lower()

def split_sentences(text):
    parts = re.split(r"[.!?]", text)
    sentences = []
    for s in parts:
        s = s.strip()
        if len(s.split()) >= 6:
            sentences.append(s + ".")
    return sentences

def get_data(q):
    rss = f"https://news.google.com/rss/search?q={q.replace(' ', '+')}"
    try:
        r = requests.get(rss, timeout=10)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"⚠ Skipping '{q}' due to network issue")
        return

    soup = BeautifulSoup(r.text, "xml")
    items = soup.find_all("item")

    for item in items:
        title = clean_html(item.title.get_text(strip=True))
        description = clean_html(item.description.get_text(strip=True))
        link = item.link.get_text(strip=True)

        for s in split_sentences(title):
            all_sentences.append([s.strip(), link])
        for s in split_sentences(description):
            all_sentences.append([s.strip(), link])

for q in queries:
    print("Fetching:", q)
    get_data(q)
    time.sleep(2)

unique = []
seen = set()

for sentence, link in all_sentences:
    key = normalize_for_dedup(sentence)
    if key not in seen:
        seen.add(key)
        unique.append([sentence, link])

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/genz_sentences.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Sentence", "Source"])
    writer.writerows(unique)

print("Total UNIQUE sentences:", len(unique))
print("Saved clean dataset as data/raw/genz_sentences.csv")