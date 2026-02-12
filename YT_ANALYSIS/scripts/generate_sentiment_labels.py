import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

df = pd.read_csv("../processed/cleaned_data.csv")

sia = SentimentIntensityAnalyzer()

def classify(text):
    score = sia.polarity_scores(str(text))["compound"]
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["cleaned_text"].apply(classify)

df.to_csv("../processed/sentiment_labeled_data.csv", index=False)

print("Sentiment labeling complete.")
print(df["sentiment"].value_counts())
print(df.groupby("phase")["sentiment"].value_counts())
