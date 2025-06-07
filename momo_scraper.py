import requests
from bs4 import BeautifulSoup
import re
import json
import urllib.parse

def scrape_iphone15_price():
    query = "iphone 15"
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2015&_isFuzzy=0&searchType=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # 找出含有商品 JSON 的 <script>
        script_tag = next((tag for tag in soup.find_all("script") if "initProductList" in tag.text), None)

        if not script_tag:
            return "❌ 找不到商品資料 script 區塊"

        # 用正則表達式擷取 JSON 內容
        match = re.search(r'var initProductList = (\[.*?\]);', script_tag.text, re.DOTALL)
        if not match:
            return "❌ momo 商品資料擷取失敗"

        products_json = json.loads(match.group(1))

        if not products_json:
            return "❌ momo 商品資料為空"

        # 擷取前 5 筆商品資訊
        results = []
        for product in products_json[:5]:
            name = product.get("goodsName")
            price = product.get("price")

            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results) if results else "❌ 找不到商品資訊"

    except Exception as e:
        return f"⚠️ momo API 錯誤：{e}"
