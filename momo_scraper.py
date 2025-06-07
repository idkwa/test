import requests
from bs4 import BeautifulSoup

def scrape_iphone15_price():
    url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=iphone%2015"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    products = soup.select(".prdListArea li")
    results = []

    for product in products[:5]:  # 只取前 5 項作為範例
        name_tag = product.select_one(".prdName")
        price_tag = product.select_one(".price")

        if name_tag and price_tag:
            name = name_tag.get_text(strip=True)
            price = price_tag.get_text(strip=True)
            results.append(f"{name} - {price}")

    return "\n".join(results) if results else "找不到商品資訊"
