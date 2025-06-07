import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_iphone15_price():
    url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2015"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # momo 商品資料藏在 <script> 內的 JSON 中
        script_tag = soup.find("script", string=re.compile("var searchData ="))
        if not script_tag:
            return "❌ 找不到商品資料 script 區塊"

        # 擷取 JSON 字串
        match = re.search(r"var searchData = ({.*?});", script_tag.string)
        if not match:
            return "❌ 無法擷取 JSON 內容"

        data = json.loads(match.group(1))
        goods = data.get("goodsInfoList", [])
        if not goods:
            return "❌ 找不到商品資訊"

        results = []
        for item in goods[:5]:
            name = item.get("goodsName")
            price = item.get("price")
            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results)

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"
