import requests
import urllib.parse

def scrape_iphone15_price():
    query = "iphone 15"
    encoded_query = urllib.parse.quote(query)
    
    url = f"https://shopee.tw/api/v4/search/search_items?keyword={encoded_query}&limit=5&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": f"https://shopee.tw/search?keyword={encoded_query}"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        data = res.json()

        items = data.get("items", [])
        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items[:5]:
            item_basic = item.get("item_basic", {})
            name = item_basic.get("name", "未知商品")
            price = item_basic.get("price", 0) // 100000  # 價格是乘以 100000 的
            results.append(f"{name} - ${price}")

        return "\n".join(results)

    except Exception as e:
        return f"⚠️ 蝦皮爬蟲錯誤：{e}"

