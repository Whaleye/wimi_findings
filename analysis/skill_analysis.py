# skill_analysis.py
import json
from collections import Counter

def analyze_skills(path="data/job_postings_with_skills.jsonl"):
    counter = Counter()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            job = json.loads(line)
            counter.update(job.get("skills", []))
    print("Top 10 skills:")
    for skill, count in counter.most_common(10):
        print(f"{skill}: {count}")
