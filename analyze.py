
import pandas as pd
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Kira3\socialshield-ai\video_history_sample.csv')
print("Loaded data:", len(df), "records\n")

df['timestamp'] = pd.to_datetime(df['watched_at'])

# Get top 5 video titles
top_titles = df['title'].value_counts().head(5)
print("🎥 Top 5 Video Titles:\n", top_titles, "\n")

print("📺 Total Videos Watched:", len(df))

df['hour'] = df['timestamp'].dt.hour
top_hours = df['hour'].value_counts().sort_index()
print("\n🕒 Watch Activity by Hour:\n", top_hours)

if 'duration' in df.columns:
    total_minutes = df['duration'].sum()
    print("\nEstimated Time Watched:", round(total_minutes / 60, 2), "hours")

# Insight Summary
print("\n🧠 INSIGHT SUMMARY:")

# ERROR: top_channels variable is not defined
# Fixed by creating top_channels from title or using top_titles
top_channels = df['title'].value_counts()  # Using title as proxy for channel

if len(top_channels) > 0 and top_channels.iloc[0] > 10:
    print(f"You're likely a fan of '{top_channels.index[0]}' — you've watched {top_channels.iloc[0]} of their videos.")

peak_hour = top_hours.idxmax()
if peak_hour >= 0:
    print(f"You watch the most during {peak_hour}:00 hours.")

if peak_hour >= 0 and peak_hour <= 6:
    print("⚠️ You tend to watch late at night — consider checking your sleep habits.")

if len(df) > 100:
    print("That's a lot of screen time this week 😅")

plt.figure(figsize=(10, 4))
top_hours.plot(kind='bar', color='skyblue')
plt.title("Watch Activity by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Number of Videos Watched")
plt.tight_layout()
plt.savefig("watch_activity_by_hour.png")
plt.show()