import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

INPUT_PATH = "data/processed/genz_sentences_cleaned.csv"
OUTPUT_PATH = "data/processed/genz_sentences_processed.csv"

df = pd.read_csv(INPUT_PATH)

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    sentence = sentence.lower()
    sentence = re.sub(r"[^a-z\s]", "", sentence)
    words = sentence.split()
    words = [w for w in words if w not in stop_words]
    words = [lemmatizer.lemmatize(w) for w in words]
    return " ".join(words)

df["processed_sentence"] = df["Sentence"].astype(str).apply(preprocess)

df.to_csv(OUTPUT_PATH, index=False)

print("Preprocessing complete")
print(f"Saved to: {OUTPUT_PATH}")
