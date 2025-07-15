# agents/content_agent.py
import os, json
from pathlib import Path
from bs4 import BeautifulSoup

def run_content_extraction():
    raw_dir = "data/raw_html"
    out_path = "data/job_postings.jsonl"
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as out_f:
        for file in os.listdir(raw_dir):
            with open(os.path.join(raw_dir, file), encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                for a in soup.find_all("a"):
                    href = a.get("href")
                    if not href: continue
                    job = {
                        "university": file.replace(".html", ""),
                        "title": a.get_text(strip=True),
                        "url": href
                    }
                    out_f.write(json.dumps(job, ensure_ascii=False) + "\n")
    print(f"✅ Parsed job links to {out_path}")
