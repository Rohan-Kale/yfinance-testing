import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as ppl
import mplfinance as mpf
import matplotlib.dates as mpdates
import datetime as dt

class GraphData:
    
    def __init__(self):
        # we can also download data for multiple tickers at one by making a list ['AAPL', 'MSFT', ...]
        self.aapl_data = yf.download("AAPL", period="3mo") 
        self.msft_data = yf.download("MSFT", period="3mo")
        self.nvda_data = yf.download("NVDA", period="3mo")
        self.required_cols = ['Open','High','Low','Close','Volume']

    
    def filter_data(self, company):
        if isinstance(company.columns, pd.MultiIndex):
            company.columns = [col[0] for col in company.columns]
        company = company.dropna(subset=self.required_cols)
        company[self.required_cols] = company[self.required_cols].apply(pd.to_numeric, errors='coerce')

        company.index = pd.to_datetime(company.index)
        
        return company

    def plot(self):
        self.aapl_data = self.aapl_data[self.required_cols]
        
        aapl_data = self.filter_data(self.aapl_data)
        msft_data = self.filter_data(self.msft_data)
        nvda_data = self.filter_data(self.nvda_data)

        axes = ppl.subplots(nrows=3, ncols=1, figsize=(12, 10), sharex=True)
        
        mpf.plot(aapl_data, type='candle', ax=axes[0], style='yahoo', axtitle='AAPL')
        mpf.plot(msft_data, type='candle', ax=axes[1], style='yahoo', axtitle='MSFT')
        mpf.plot(nvda_data, type='candle', ax=axes[2], style='yahoo', axtitle='NVDA')

        ppl.tight_layout()
        ppl.show()

test = GraphData()

test.plot()






# ppl.plot(msft_data['Close'], label = "MSFT", color='blue')
# ppl.plot(aapl_data['Close'], label = "AAPL", color='red')
# ppl.plot(nvda_data['Close'], label = "NVDA", color='green')
# ppl.xlabel("Date")
# ppl.ylabel("Stock Price (USD)")
# ppl.title("Stock Prices for 2025")

# ppl.legend()
# ppl.grid(True)
# ppl.show()

