import requests

def scrape_iphone15_price():
    url = "https://tw.buy.yahoo.com/api/v1/display/search"
    params = {
        "p": "iphone 15",
        "cc": "TW",
        "device": "desktop",
        "module": "all",
        "fl": "tw"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()
        data = res.json()

        # 商品清單通常在 data["sections"][0]["items"]
        sections = data.get("sections", [])
        if not sections or "items" not in sections[0]:
            return "❌ 找不到商品資訊"

        items = sections[0]["items"]
        results = []

        for item in items[:5]:  # 前 5 筆
            name = item.get("name")
            price = item.get("price", {}).get("value") or item.get("price")

            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results) if results else "❌ 商品清單為空"

    except Exception as e:
        return f"⚠️ Yahoo API 錯誤：{e}"
