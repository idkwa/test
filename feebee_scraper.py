import requests

def scrape_iphone15_price():
    url = "https://tw.buy.yahoo.com/api/v1/display/search"
    params = {
        "p": "iphone 15",
        "fl": "tw",
        "device": "desktop"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        res = requests.get(url, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()

        items = []
        for section in data.get("sections", []):
            items.extend(section.get("items", []))

        if not items:
            return "❌ 找不到商品資訊"

        results = []
        for item in items[:5]:  # 前 5 筆商品
            name = item.get("name")
            price = item.get("price", {}).get("value") or item.get("price")
            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results) if results else "❌ 商品清單為空"

    except Exception as e:
        return f"⚠️ Yahoo API 錯誤：{e}"
