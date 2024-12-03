import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_pull_requests(state):
    """
    Example of return:
    [
        {"title": "Add useful stuff", "num": 56, "link": "https://github.com/boto/boto3/pull/56"},
        {"title": "Fix something", "num": 57, "link": "https://github.com/boto/boto3/pull/57"},
    ]
    """
    # Write 
    # ya hice add y lo modico luego

    return []
# manita linda