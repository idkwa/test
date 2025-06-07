from flask import Flask, request, jsonify
from feebee_scraper import scrape_iphone15_price
import requests

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1379337992317042688/aqp4lMDPPgrRFfxuYqhQSMiDKCht7-oP8hdCIRuDxNpJaJL90HwPzVFgFLsqtYlRrJcO"

app = Flask(__name__)

def send_to_discord(message):
    data = {"content": message}
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print("傳送失敗", response.text)

@app.route("/webhook", methods=["POST"])
def trigger_scraper():
    price_info = scrape_iphone15_price()
    send_to_discord(f"📱 iPhone 15 價格更新：\n{price_info}")
    return jsonify({"status": "ok", "message": "已送出 Discord"})

