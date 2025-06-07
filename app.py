from flask import Flask, request
from feebee_scraper import scrape_ptt_ios_titles
import requests
import os

app = Flask(__name__)

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

@app.route("/webhook", methods=["POST"])
def webhook():
    content = scrape_iphone15_price()
    payload = {
        "content": f"📱 iPhone 15 價格更新：\n{content}"
    }
    requests.post(DISCORD_WEBHOOK_URL, json=payload)
    return {"status": "success"}

if __name__ == "__main__":
    app.run()
