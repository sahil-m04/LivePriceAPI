from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.utils.fetch_finnhub import fetch_finnhub_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # adjust for your frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/price")
async def get_foreign_price(symbols: str = Query(...)):
    symbol_list = symbols.split(",")
    prices = {}
    for sym in symbol_list:
        prices[sym] = await fetch_finnhub_price(sym)
    return prices
