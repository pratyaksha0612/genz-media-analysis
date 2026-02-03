import requests
from bs4 import BeautifulSoup
import csv
import re
import time
import unicodedata
import os
from datetime import datetime


queries = [
    # Core Gen Z
    "Gen Z",
    "Generation Z",
    "Gen Z youth",
    "Gen Z students",
    "Gen Z activism",

    # Youth & society
    "youth movement",
    "youth activism",
    "student movement",
    "student protests",
    "youth unrest",

    # Politics & protests
    "youth protests",
    "student protests Asia",
    "political protests youth",
    "election protests youth",
    "government protests youth",

    # Nepal-specific 
    "Nepal youth",
    "Nepal Gen Z",
    "Nepal students",
    "Nepal youth movement",
    "Nepal protests",
    "Nepal political unrest"
]


all_sentences = []

def clean_html(text):
    text = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\.\S+", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def normalize_for_dedup(text):
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"[–—−]", "-", text)
    text = re.sub(r"[\"'‘’“”]", "", text)
    text = re.sub(r"\s*-\s*", " - ", text)
    text = re.sub(r"\s+", " ", text)
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

def parse_pub_date(pub_date_str):
    """
    Convert RSS pubDate string to YYYY-MM-DD format.
    """
    try:
        dt = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %Z")
        return dt.date().isoformat()
    except Exception:
        return None

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

        pub_date_tag = item.find("pubDate")
        published_date = (
            parse_pub_date(pub_date_tag.get_text(strip=True))
            if pub_date_tag else None
        )

        for s in split_sentences(title):
            all_sentences.append([s.strip(), link, published_date])
        for s in split_sentences(description):
            all_sentences.append([s.strip(), link, published_date])

for q in queries:
    print("Fetching:", q)
    get_data(q)
    time.sleep(2)

unique = []
seen = set()

for sentence, link, published_date in all_sentences:
    key = normalize_for_dedup(sentence)
    if key not in seen:
        seen.add(key)
        unique.append([sentence, link, published_date])

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/genz_sentences.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Sentence", "Source", "Published_Date"])
    writer.writerows(unique)

print("Total UNIQUE sentences:", len(unique))
print("Saved clean dataset as data/raw/genz_sentences.csv")
