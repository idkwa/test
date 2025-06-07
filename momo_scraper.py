import requests
from bs4 import BeautifulSoup

def scrape_iphone15_price():
    url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2015"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        # 新的商品區塊選擇器
        items = soup.select('li.goodsItem')
        if not items:
            return "❌ 找不到商品資訊（無商品區塊）"

        results = []

        for item in items[:5]:  # 限制前 5 筆商品
            name_tag = item.select_one("h3.prdName")
            price_tag = item.select_one("b.price")

            if name_tag and price_tag:
                name = name_tag.get_text(strip=True)
                price = price_tag.get_text(strip=True)
                results.append(f"{name} - ${price}")

        return "\n".join(results) if results else "❌ 找不到商品資訊（商品資料不完整）"

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"

