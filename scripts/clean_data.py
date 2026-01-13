import pandas as pd
import re

INPUT_CSV = "data/raw/genz_sentences.csv"
OUTPUT_CSV = "data/processed/genz_sentences_cleaned.csv"

df = pd.read_csv(INPUT_CSV)

df = df[["Sentence", "Source"]]

def normalize_sentence(text):
    text = str(text).lower()
    text = re.sub(r"[’‘“”\"']", "", text)   # remove quotes
    text = re.sub(r"[^a-z0-9\s]", "", text) # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["normalized"] = df["Sentence"].apply(normalize_sentence)

df = df.drop_duplicates(subset="normalized")

df = df.drop(columns=["normalized"])
df = df.reset_index(drop=True)

df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")

print("✅ Cleaning complete")
print(f"📄 Original file  : {INPUT_CSV}")
print(f"📄 Cleaned file   : {OUTPUT_CSV}")
print(f"🔢 Clean rows     : {len(df)}")
