import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

async def fetch_finnhub_price(symbol: str) -> float:
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            return float(data.get("c", 0.0))  
    except Exception as e:
        print(f"Finnhub fetch error: {e}")
        return 0.0