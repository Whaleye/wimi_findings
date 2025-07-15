# db_writer.py
import sqlite3, json

def save_to_sqlite(jsonl_path, db_path="data/jobs.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS job_postings (
        university TEXT,
        title TEXT,
        url TEXT,
        skills TEXT
    )""")
    with open(jsonl_path, "r", encoding="utf-8") as f:
        for line in f:
            job = json.loads(line)
            cur.execute("INSERT INTO job_postings VALUES (?, ?, ?, ?)",
                (job["university"], job["title"], job["url"], ", ".join(job["skills"])))
    conn.commit()
    conn.close()
    print(f"✅ Saved records to {db_path}")
