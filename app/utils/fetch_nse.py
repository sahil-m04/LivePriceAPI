import httpx
from bs4 import BeautifulSoup

def fetch_nse_price(symbol: str) -> float:
    url = f"https://www.nseindia.com/get-quotes/equity?symbol={symbol}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.nseindia.com",
        "Accept-Language": "en-US,en;q=0.9",
    }

    try:
        with httpx.Client(headers=headers, timeout=10) as client:
            client.get("https://www.nseindia.com")  # for cookies
            response = client.get(url)
            soup = BeautifulSoup(response.text, "lxml")

            # Extract value — might need updating depending on actual HTML
            price_tag = soup.select_one(".security-quote .price")
            return float(price_tag.text.replace(",", "")) if price_tag else 0.0
    except Exception as e:
        print(f"NSE fetch error: {e}")
        return 0.0
