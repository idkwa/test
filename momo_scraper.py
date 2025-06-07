import requests

def scrape_iphone15_price():
    url = "https://www.momoshop.com.tw/api/v1/search"
    params = {
        "searchType": 1,
        "keyword": "iphone 15",
        "curPage": 1,
        "pageSize": 5
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.momoshop.com.tw/"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    results = []
    for item in data.get("rtnSearchResult", {}).get("goodsInfoList", []):
        name = item.get("goodsName", "無名稱")
        price = item.get("price", "無價格")
        results.append(f"{name} - ${price}")

    return "\n".join(results) if results else "找不到商品資訊"
