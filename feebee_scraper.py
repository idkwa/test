import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_iphone15_price():
    query = "iphone 15"
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://tw.buy.yahoo.com/search/product?p={encoded_query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        items = soup.select("li[data-qa-locator='product-item']")  # 更新選擇器
        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items[:5]:
            name_tag = item.select_one("span.sc-6n68ef-0")  # 商品名稱
            price_tag = item.select_one("span.sc-1e4emg8-1")  # 價格文字

            if name_tag and price_tag:
                name = name_tag.get_text(strip=True)
                price = price_tag.get_text(strip=True)
                results.append(f"{name} - {price}")

        return "\n".join(results) if results else "❌ 商品清單為空"

    except Exception as e:
        return f"⚠️ Yahoo 爬蟲錯誤：{e}"
