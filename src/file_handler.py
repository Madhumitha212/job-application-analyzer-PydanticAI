import json
import os
from datetime import datetime

FILE_NAME = "applications.json"

def save_data(data):
    records = []

    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                records = json.load(f)
        except:
            records = []

    data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    records.append(data)

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=4)