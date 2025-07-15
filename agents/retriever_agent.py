# agents/retriever_agent.py
import yaml, requests
from pathlib import Path

def run_retriever():
    with open("config/universities.yaml", "r", encoding="utf-8") as f:
        universities = yaml.safe_load(f)["universities"]

    Path("data/raw_html").mkdir(parents=True, exist_ok=True)
    for uni in universities:
        name = uni["alias"] or uni["name"]
        url = uni["base_url"]
        if not url:
            print(f"⚠️ Skipping {name}: no base_url")
            continue
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            with open(f"data/raw_html/{name}.html", "w", encoding="utf-8") as f:
                f.write(resp.text)
            print(f"✅ Retrieved HTML for {name}")
        except Exception as e:
            print(f"❌ Failed to retrieve {name}: {e}")