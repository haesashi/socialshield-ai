import json
import pandas as pd
import os

def load_history(json_path=r'C:\Users\Kira3\Downloads\takeout-20250428T162821Z-001 (1)\Takeout\YouTube and YouTube Music\history\watch-history.json', 
                out_csv='data/video_history.csv'):
    # Load JSON data from the given path
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"The file '{json_path}' does not exist.")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    records = []
    for item in data:
        # Only entries with a video URL
        url = item.get('titleUrl')
        if not url or 'watch?v=' not in url:
            continue
        records.append({
            'title': item.get('title', ''),
            'video_id': url.split('v=')[-1],
            'url': url,
            'watched_at': item.get('time', '')
        })

    # Create DataFrame & ensure the output folder exists
    output_dir = os.path.dirname(out_csv)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    
    df = pd.DataFrame(records)
    df.to_csv(out_csv, index=False)
    print(f"Saved {len(records)} records to '{out_csv}'")

if __name__ == "__main__":
    load_history()

