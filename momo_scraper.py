import requests

def scrape_iphone15_price():
    try:
        url = "https://www.momoshop.com.tw/api/v1/search"
        params = {
            "searchType": 1,
            "keyword": "iphone 15",
            "curPage": 1,
            "pageSize": 5
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.momoshop.com.tw/",
            "X-Requested-With": "XMLHttpRequest"
        }

        res = requests.get(url, params=params, headers=headers)
        res.raise_for_status()  # 非 200 則拋出錯誤

        try:
            data = res.json()
        except Exception:
            print("⚠️ 非 JSON 回傳內容：")
            print(res.text[:500])  # 印出前 500 字協助 debug
            return "❌ momo 回傳非 JSON 格式，可能被擋了"

        goods = data.get("rtnSearchResult", {}).get("goodsInfoList", [])

        if not goods:
            return "找不到商品資訊（API 回傳空資料）"

        results = [f"{item['goodsName']} - ${item['price']}" for item in goods]
        return "\n".join(results)

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"
print(res.text[:500])

