
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\Users\Kira3\socialshield-ai\video_history.csv")
titles = df['title'].dropna().astype(str)

vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(titles)

k = 5  
model = KMeans(n_clusters=k, random_state=42)
df['cluster'] = model.fit_predict(X)

os.makedirs("data", exist_ok=True)

df.to_csv("data/video_clusters.csv", index=False)
print("✅ Clustered video data saved to 'data/video_clusters.csv'")

df['cluster'].value_counts().sort_index().plot(kind='bar')
plt.title("Video Count per Cluster")
plt.xlabel("Cluster")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("cluster_distribution.png")
plt.show()