# retriever.py
from pathlib import Path
import yaml, requests
from mcp import BaseAgent, Metadata, ToolOutput

class RetrieverAgent(BaseAgent):
    @property
    def metadata(self) -> Metadata:
        return Metadata(
            name="retriever_agent",
            description="Crawl configured university job URLs and save HTML."
        )

    def run(self, **kwargs) -> ToolOutput:
        with open("config/universities.yaml", "r", encoding="utf-8") as f:
            universities = yaml.safe_load(f)["universities"]

        results = []
        Path("data/raw_html").mkdir(parents=True, exist_ok=True)
        for uni in universities:
            name = uni["alias"] or uni["name"]
            url = uni["base_url"]
            if not url:
                results.append(f"❌ Skipped {name} (no base_url)")
                continue

            try:
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                html_path = f"data/raw_html/{name}.html"
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(resp.text)
                results.append(f"✅ {name} -> saved to {html_path}")
            except Exception as e:
                results.append(f"❌ {name} failed: {e}")
        
        return ToolOutput(output="\n".join(results))
