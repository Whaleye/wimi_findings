# utils/llm_tools.py
import random

def extract_skills_from_text(text):
    # 示例：模拟 LLM 返回
    dummy_skills = ["Python", "Machine Learning", "Data Analysis", "Deep Learning"]
    return random.sample(dummy_skills, k=random.randint(1, 3))