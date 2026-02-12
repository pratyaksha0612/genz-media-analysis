import pandas as pd
import re

input_path = "../raw/youtube_nepal_genz_dataset.csv"
output_path = "../processed/cleaned_data.csv"

df = pd.read_csv(input_path)

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"\@\w+|\#", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

df["cleaned_text"] = df["text"].apply(clean_text)

df = df[df["cleaned_text"].str.strip() != ""]
df = df.drop_duplicates(subset="cleaned_text")

df.to_csv(output_path, index=False)

print("Cleaning complete.")
print("Total rows after cleaning:", len(df))
print(df["phase"].value_counts())
