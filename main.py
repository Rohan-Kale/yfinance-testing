import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as ppl
import mplfinance as mpf
import matplotlib.dates as mpdates
import datetime as dt


# Download AAPL only
aapl_data = yf.download("AAPL", period="3mo") 
msft_data = yf.download("MSFT", period="3mo")
nvda_data = yf.download("NVDA", period="3mo")


if isinstance(aapl_data.columns, pd.MultiIndex):
    aapl_data.columns = [col[0] for col in aapl_data.columns]
print("Columns:", aapl_data.columns.tolist())

required_cols = ['Open','High','Low','Close','Volume']
aapl_data = aapl_data[required_cols]

aapl_data = aapl_data.dropna(subset=required_cols)

aapl_data[required_cols] = aapl_data[required_cols].apply(pd.to_numeric, errors='coerce')
aapl_data = aapl_data.dropna(subset=required_cols)

aapl_data.index = pd.to_datetime(aapl_data.index)

mpf.plot(
    aapl_data,
    type='candle',
    style='yahoo',
    title='AAPL Candlestick Chart',
)

ppl.plot(msft_data['Close'], label = "MSFT", color='blue')
ppl.plot(aapl_data['Close'], label = "AAPL", color='red')
ppl.plot(nvda_data['Close'], label = "NVDA", color='green')
ppl.xlabel("Date")
ppl.ylabel("Stock Price (USD)")
ppl.title("Stock Prices for 2025")

ppl.legend()
ppl.grid(True)
ppl.show()

