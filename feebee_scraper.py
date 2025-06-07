import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import random

def scrape_iphone15_price():
    query = "iphone 15"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://feebee.com.tw/s/?q={encoded_query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.select("li.productItem")
        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items[:5]:
            name_tag = item.select_one(".productItem__title")
            price_tag = item.select_one(".productItem__price--highlight")

            if name_tag and price_tag:
                name = name_tag.get_text(strip=True)
                price = price_tag.get_text(strip=True)
                results.append(f"{name} - {price}")

            # 加入隨機延遲，避免觸發反爬蟲機制
            time.sleep(random.uniform(1, 3))

        return "\n".join(results) if results else "❌ 商品清單為空"

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"
