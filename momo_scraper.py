import requests

def scrape_iphone15_price():
    url = "https://m.momoshop.com.tw/api/momoSearch.jsp"
    params = {
        "searchKeyword": "iphone 15",
        "curPage": "1",
        "pageSize": "20"
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    try:
        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()
        data = res.json()

        goods = data.get("rtnSearchData", {}).get("goodsInfoList", [])
        if not goods:
            return "❌ momo 查不到商品資料"

        results = []
        for item in goods[:5]:  # 只取前 5 筆商品
            name = item.get("goodsName")
            price = item.get("price")
            if name and price:
                results.append(f"{name} - ${price}")

        return "\n".join(results)

    except Exception as e:
        return f"⚠️ momo API 錯誤：{e}"
