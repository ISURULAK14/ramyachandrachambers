#!/usr/bin/env python3
"""
Automated IndexNow Submitter for https://ramyachandrachambers.com/
Notifies search engines (Bing, Yandex, Seznam, Naver) immediately when content changes.
"""
import urllib.request
import json
import ssl

HOST = "ramyachandrachambers.com"
KEY = "e4f971b3e8c24d1a980562e84c31ab7d"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URL_LIST = [
    "https://ramyachandrachambers.com/",
    "https://ramyachandrachambers.com/about.html",
    "https://ramyachandrachambers.com/services.html",
    "https://ramyachandrachambers.com/practice-areas.html",
    "https://ramyachandrachambers.com/testimonials.html",
    "https://ramyachandrachambers.com/contact.html"
]

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

def submit():
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": URL_LIST
    }
    data = json.dumps(payload).encode('utf-8')
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "User-Agent": "IndexNowSubmitter/1.0 (ramyachandrachambers.com)"
    }

    ctx = ssl.create_default_context()

    for endpoint in ENDPOINTS:
        print(f"Submitting to {endpoint}...")
        try:
            req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=10, context=ctx) as response:
                print(f"  Response [{response.status}]: {response.reason}")
        except Exception as e:
            print(f"  Notice: {e} (Normal if DNS/Domain is live on Cloudflare)")

if __name__ == "__main__":
    submit()
