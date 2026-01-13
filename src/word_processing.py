import pandas as pd
import re
import string

INPUT_FILE = "data/processed/genz_sentences_processed.csv"
OUTPUT_FILE = "data/processed/genz_tokens.csv"

# Basic English stopwords
STOPWORDS = {
    "the", "is", "and", "to", "of", "in", "for", "on", "with", "as",
    "by", "at", "from", "that", "this", "it", "are", "was", "be"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text):
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    return tokens

def main():
    df = pd.read_csv(INPUT_FILE)

    df["clean_text"] = df["processed_sentence"]
    df["tokens"] = df["clean_text"].apply(tokenize)

    df[["Sentence", "tokens"]].to_csv(OUTPUT_FILE, index=False)

    print("Tokenized data saved to:", OUTPUT_FILE)
    print("Total sentences processed:", len(df))

if __name__ == "__main__":
    main()
