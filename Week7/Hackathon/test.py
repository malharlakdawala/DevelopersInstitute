# import datetime as dt
# import yfinance as yf
# import pandas as pd
#
# stocks = ["AMZN", "MSFT", "INTC", "GOOG", "INFY.NS", "3988.HK"]
# start = dt.datetime.today() - dt.timedelta(360)
# end = dt.datetime.today()
# cl_price = pd.DataFrame()  # empty dataframe which will be filled with closing prices of each stock
# ohlcv_data = {}  # empty dictionary which will be filled with ohlcv dataframe for each ticker
#
# # looping over tickers and creating a dataframe with close prices
# for ticker in stocks:
#     cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
#
# # looping over tickers and storing OHLCV dataframe in dictionary
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()



