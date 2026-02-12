from googleapiclient.discovery import build
import pandas as pd
from datetime import datetime
import socket

socket.setdefaulttimeout(15)

API_KEY = "AIzaSyDzm9law47WOrL9f46O70_J-F51Thidlus"

youtube = build("youtube", "v3", developerKey=API_KEY)

PROTEST_START = datetime(2025, 9, 8)
PROTEST_END   = datetime(2025, 9, 13)

baseline_queries = [
    "Gen Z discussion 2025",
    "Youth political debate 2025"
]

protest_queries = [
    "Nepal protest September 2025"
]

rows = []

def get_phase(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    if date < PROTEST_START:
        return "before"
    elif PROTEST_START <= date <= PROTEST_END:
        return "during"
    else:
        return "after"

def collect_comments(query, max_videos=2, max_pages=2):
    print("Query:", query)

    search_response = youtube.search().list(
        q=query,
        part="id",
        type="video",
        maxResults=max_videos,
        order="relevance"
    ).execute()

    for item in search_response.get("items", []):
        video_id = item["id"]["videoId"]
        print("Video:", video_id)

        next_page_token = None
        page_count = 0

        while page_count < max_pages:
            comment_response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
                textFormat="plainText"
            ).execute()

            for comment in comment_response.get("items", []):
                snippet = comment["snippet"]["topLevelComment"]["snippet"]
                text = snippet["textDisplay"]
                date = snippet["publishedAt"]

                rows.append({
                    "text": text,
                    "date": date,
                    "phase": get_phase(date),
                    "source": "youtube"
                })

            next_page_token = comment_response.get("nextPageToken")
            page_count += 1

            if not next_page_token:
                break

print("Collecting baseline...")
for query in baseline_queries:
    collect_comments(query)

print("Collecting protest...")
for query in protest_queries:
    collect_comments(query, max_videos=5)

df = pd.DataFrame(rows)
df.drop_duplicates(subset="text", inplace=True)

df.to_csv("YT_ANALYSIS/raw/youtube_nepal_genz_dataset.csv", index=False)

print("Dataset saved.")
print("Total rows:", len(df))
print(df["phase"].value_counts())
