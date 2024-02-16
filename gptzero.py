# gptzero.py
import requests
from api_key import key

def analyze_with_gptzero(document):
    url = "https://api.gptzero.me/v2/predict/text"

    payload = {
        "document": document,
        "version": "2024-01-09"
    }
    headers = {
        "x-api-key": key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
