"""
Simulates user thought input and saves it to a structured JSON file.
"""

import json
from datetime import datetime

def get_thought_input():
    print("Enter your thought stream (type 'exit' to finish):")
    thoughts = []
    while True:
        line = input("> ")
        if line.strip().lower() == "exit":
            break
        thoughts.append({
            "timestamp": datetime.now().isoformat(),
            "text": line.strip()
        })
    return thoughts

def save_thoughts(thoughts, file_path="data/thoughts_log.json"):
    import os
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        json.dump(thoughts, f, indent=2)

if __name__ == "__main__":
    thoughts = get_thought_input()
    save_thoughts(thoughts)
