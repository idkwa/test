import requests

def scrape_iphone15_price():
    url = "https://tw.buy.yahoo.com/api/v8/storage/search"
    params = {
        "p": "iphone 15",
        "qt": "product",
        "page": "1",
        "per_page": "5"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "x-requested-with": "XMLHttpRequest"
    }

    try:
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()
        data = res.json()

        items = data.get("records", [])
        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items:
            name = item.get("name")
            price = item.get("price", {}).get("value")
            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results) if results else "❌ 商品清單為空"

    except Exception as e:
        return f"⚠️ Yahoo API 錯誤：{e}"
