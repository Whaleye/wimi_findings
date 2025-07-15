# skill_dashboard.py
import streamlit as st
import json
from collections import Counter

st.title("📊 Skill Dashboard")

with open("data/job_postings_with_skills.jsonl", "r", encoding="utf-8") as f:
    all_skills = Counter()
    for line in f:
        job = json.loads(line)
        all_skills.update(job.get("skills", []))

most_common = all_skills.most_common(20)
st.bar_chart({k: v for k, v in most_common})