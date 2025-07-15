# agents/skill_agent.py
import json
from pathlib import Path
from utils.llm_tools import extract_skills_from_text

def run_skill_extraction():
    input_path = "data/job_postings.jsonl"
    output_path = "data/job_postings_with_skills.jsonl"
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(input_path, "r", encoding="utf-8") as in_f, \
         open(output_path, "w", encoding="utf-8") as out_f:
        for line in in_f:
            job = json.loads(line)
            job_desc = job.get("description", "")
            skills = extract_skills_from_text(job_desc)
            job["skills"] = skills
            out_f.write(json.dumps(job, ensure_ascii=False) + "\n")
    print(f"✅ Extracted skills to {output_path}")
