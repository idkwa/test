import requests
from bs4 import BeautifulSoup

def scrape_ptt_ios_titles():
    url = "https://www.ptt.cc/bbs/iOS/index.html"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        titles = soup.select("div.title a")
        if not titles:
            return "❌ 找不到文章標題"

        results = []
        for title in titles[:5]:  # 取前 5 篇
            results.append(title.get_text(strip=True))

        return "\n".join(results)

    except Exception as e:
        return f"⚠️ 爬蟲錯誤：{e}"
