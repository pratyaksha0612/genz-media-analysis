import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load dataset
df = pd.read_csv("YT_ANALYSIS/raw/youtube_nepal_genz_dataset.csv")

sia = SentimentIntensityAnalyzer()

# Compute sentiment
df["compound"] = df["text"].apply(lambda x: sia.polarity_scores(str(x))["compound"])

# Classify sentiment
def classify(score):
    if score >= 0.05:
        return "positive"
    elif score <= -0.05:
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["compound"].apply(classify)

# Phase-wise analysis
phase_summary = df.groupby("phase")["compound"].mean()
sentiment_distribution = df.groupby(["phase", "sentiment"]).size().unstack(fill_value=0)

print("\nAverage Compound Score by Phase:")
print(phase_summary)

print("\nSentiment Distribution by Phase:")
print(sentiment_distribution)
