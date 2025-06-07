import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_iphone15_price():
    query = "iphone 15"
    encoded_query = urllib.parse.quote(query)
    url = f"http://m.momoshop.com.tw/mosearch/{encoded_query}.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.select("ul.prdList li")
        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items[:5]:  # 只取前 5 筆商品
            name_tag = item.select_one("p.prdName")
            price_tag = item.select_one("b.price")

            if name_tag and price_tag:
                name = name_tag.get_text(strip=True)
                price = price_tag.get_text(strip=True)
                results.append(f"{name} - ${price}")

        return "\n".join(results)

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"
