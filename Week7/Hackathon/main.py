from renko_macd import function
import numpy as np
import pandas as pd
from stocktrends import Renko
import statsmodels.api as sm
#from alpha_vantage.timeseries import TimeSeries
import copy
import datetime as dt
import yfinance as yf

ohlc_intraday = {}
stocks = ["SBIN.NS","JSWSTEEL.BO","JINDALSTEL.BO","WIPRO.BO","NTPC.BO"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
cl_price = pd.DataFrame()  # empty dataframe which will be filled with closing prices of each stock
#ohlc_intraday = {}  # empty dictionary which will be filled with ohlcv dataframe for each ticker

a = yf.download("AMZN", start, end)

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in stocks:
    ohlc_intraday[ticker] = yf.download(ticker, start, end, interval='5m')
    del ohlc_intraday[ticker]["Close"]
    ohlc_intraday[ticker].columns=["Open","High","Low","Adj Close","Volume"]
        
tickers = ohlc_intraday.keys()
