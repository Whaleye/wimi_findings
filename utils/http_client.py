# utils/http_client.py
import requests

def fetch_html(url, timeout=10):
    headers = {"User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers, timeout=timeout)
    resp.raise_for_status()
    return resp.text