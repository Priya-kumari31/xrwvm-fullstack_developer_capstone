import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv("backend_url", default="http://host.docker.internal:3030")
sentiment_analyzer_url = os.getenv("sentiment_analyzer_url", default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        params = "?"
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    response = requests.get(backend_url + endpoint + params)
    return response.json()

def post_review(data_dict):
    response = requests.post(
        backend_url + "/insert_review",
        json=data_dict,
        headers={"Content-Type": "application/json"}
    )
    return response.json()
