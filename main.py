from agents.retriever_agent import run_retriever
from agents.content_agent import run_content_extraction
from agents.skill_agent import run_skill_extraction

if __name__ == "__main__":
    run_retriever()
    run_content_extraction()
    run_skill_extraction()
    print("✅ All steps completed.")