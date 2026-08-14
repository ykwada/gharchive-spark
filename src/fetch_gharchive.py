import requests
import os

TARGET_DATE = "2026-08-08"sd

def fetch_gharchive():
    for t in range(24):
        url = f"https://data.gharchive.org/{TARGET_DATE}-{t}.json.gz"

        response = requests.get(url)
        response.raise_for_status()

        path = f"/app/data/raw/{TARGET_DATE}-{t}.json.gz"

        dirname = os.path.dirname(path)
        os.makedirs(dirname, exist_ok=True)

        with open(path, "wb") as f:
            f.write(response.content)

if __name__ == "__main__":
    fetch_gharchive()