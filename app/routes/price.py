from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.nseindia.com/"
}

@app.get("/price")
async def get_price(symbols: str = Query(...)):
    result = {}
    async with httpx.AsyncClient(headers=HEADERS, timeout=10.0) as client:
        # 1. Hit NSE homepage
        await client.get("https://www.nseindia.com")

        # 2. Loop through each symbol
        for symbol in symbols.split(","):
            try:
                res = await client.get(f"https://www.nseindia.com/api/quote-equity?symbol={symbol.upper()}")
                data = res.json()
                price = data["priceInfo"]["lastPrice"]
                result[symbol.upper()] = price
            except Exception as e:
                print(f"Failed to fetch {symbol}: {e}")
                result[symbol.upper()] = 0.0

    return result
