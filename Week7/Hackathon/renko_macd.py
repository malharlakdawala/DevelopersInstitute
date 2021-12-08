# =============================================================================
# renko + macd
# =============================================================================

import numpy as np
import pandas as pd
from stocktrends import Renko
import statsmodels.api as sm
import copy
import datetime as dt
import yfinance as yf
from kc_orders import OrderPlace
import time
from kiteconnect import KiteConnect
import os




def MACD(DF,a,b,c):
    """function to calculate MACD
       typical values a = 12; b =26, c =9"""
    df = DF.copy()
    df["MA_Fast"]=df["Adj Close"].ewm(span=a,min_periods=a).mean()
    df["MA_Slow"]=df["Adj Close"].ewm(span=b,min_periods=b).mean()
    df["MACD"]=df["MA_Fast"]-df["MA_Slow"]
    df["Signal"]=df["MACD"].ewm(span=c,min_periods=c).mean()
    df.dropna(inplace=True)
    return (df["MACD"],df["Signal"])

def ATR(DF,n):
    "function to calculate True Range and Average True Range"
    df = DF.copy()
    df['H-L']=abs(df['High']-df['Low'])
    df['H-PC']=abs(df['High']-df['Adj Close'].shift(1))
    df['L-PC']=abs(df['Low']-df['Adj Close'].shift(1))
    df['TR']=df[['H-L','H-PC','L-PC']].max(axis=1,skipna=False)
    df['ATR'] = df['TR'].rolling(n).mean()
    #df['ATR'] = df['TR'].ewm(span=n,adjust=False,min_periods=n).mean()
    df2 = df.drop(['H-L','H-PC','L-PC'],axis=1)
    return df2

def slope(ser,n):
    "function to calculate the slope of n consecutive points on a plot"
    slopes = [i*0 for i in range(n-1)]
    for i in range(n,len(ser)+1):
        y = ser[i-n:i]
        x = np.array(range(n))
        y_scaled = (y - y.min())/(y.max() - y.min())
        x_scaled = (x - x.min())/(x.max() - x.min())
        x_scaled = sm.add_constant(x_scaled)
        model = sm.OLS(y_scaled,x_scaled)
        results = model.fit()
        slopes.append(results.params[-1])
    slope_angle = (np.rad2deg(np.arctan(np.array(slopes))))
    return np.array(slope_angle)

def renko_DF(DF):
    "function to convert ohlc data into renko bricks"
    df = DF.copy()
    df.reset_index(inplace=True)
    df = df.iloc[:,[0,1,2,3,4,5]]
    df.columns = ["date","open","high","low","close","volume"]
    df2 = Renko(df)
    df2.brick_size = max(0.5,round(ATR(DF,120)["ATR"][-1],0))
    renko_df = df2.get_ohlc_data()
    renko_df["bar_num"] = np.where(renko_df["uptrend"]==True,1,np.where(renko_df["uptrend"]==False,-1,0))
    for i in range(1,len(renko_df["bar_num"])):
        if renko_df["bar_num"][i]>0 and renko_df["bar_num"][i-1]>0:
            renko_df["bar_num"][i]+=renko_df["bar_num"][i-1]
        elif renko_df["bar_num"][i]<0 and renko_df["bar_num"][i-1]<0:
            renko_df["bar_num"][i]+=renko_df["bar_num"][i-1]
    renko_df.drop_duplicates(subset="date",keep="last",inplace=True)
    return renko_df


def CAGR(DF):
    "function to calculate the Cumulative Annual Growth Rate of a trading strategy"
    df = DF.copy()
    df["cum_return"] = (1 + df["ret"]).cumprod()
    n = len(df)/(252*78)
    CAGR = (df["cum_return"].tolist()[-1])**(1/n) - 1
    return CAGR

def volatility(DF):
    "function to calculate annualized volatility of a trading strategy"
    df = DF.copy()
    vol = df["ret"].std() * np.sqrt(252*78)
    return vol

def sharpe(DF,rf):
    "function to calculate sharpe ratio ; rf is the risk free rate"
    df = DF.copy()
    sr = (CAGR(df) - rf)/volatility(df)
    return sr


def max_dd(DF):
    "function to calculate max drawdown"
    df = DF.copy()
    df["cum_return"] = (1 + df["ret"]).cumprod()
    df["cum_roll_max"] = df["cum_return"].cummax()
    df["drawdown"] = df["cum_roll_max"] - df["cum_return"]
    df["drawdown_pct"] = df["drawdown"]/df["cum_roll_max"]
    max_dd = df["drawdown_pct"].max()
    return max_dd

# Download historical data for for NIFTY 100 via Yahoo finance


#stocks = ["SBIN.NS","JSWSTEEL.BO","JINDALSTEL.BO","WIPRO.BO","NTPC.BO","BANKBARODA.BO","ADANIENT.BO","AMBUJACEM.BO","APOLLOHOSP.BO","BOSCHLTD.BO","ULTRACEMCO.BO","DABUR.BO","DRREDDY.BO","EICHERMOT.BO","MUTHOOTFIN.BO","HAVELLS.BO","HCLTECH.BO","HEROMOTOCO.BO","HINDALCO.BO","HINDUNILVR.BO","ICICIBANK.BO","LT.BO","PNB.BO","NESTLEIND.BO","NMDC.BO","BANKBARODA.NS","SBIN.BO","PEL.BO","TORNTPHARM.BO","AUROPHARMA.BO","TATASTEEL.BO","BAJAJ-AUTO.BO","BAJAJFINSV.BO","COALINDIA.BO","COLPAL.BO","RELIANCE.BO","PIIND.BO","HINDPETRO.BO","BAJAJHLDNG.BO","ADANIPORTS.NS","TATAMTRDVR.BO","ADANIPORTS.BO","PGHH.NS","CHOLAFIN.NS","DRREDDY.NS","HDFC.NS","SAIL.BO","DIVISLAB.NS","GODREJCP.NS","BPCL.NS","TCS.NS","MARUTI.NS","NAUKRI.BO","BAJAJHLDNG.NS","IOC.NS","JINDALSTEL.NS","KOTAKBANK.NS","BERGEPAINT.BO","BHARTIARTL.NS","JUBLFOOD.NS","INDIGO.NS","CADILAHC.NS","HCLTECH.NS","CADILAHC.BO","HEROMOTOCO.NS","AUROPHARMA.NS","PEL.NS","HINDUNILVR.NS","TECHM.NS","SHREECEM.BO","ASIANPAINT.NS","ULTRACEMCO.NS","SHREECEM.NS","EICHERMOT.NS","IGL.NS","MUTHOOTFIN.NS","JSWSTEEL.NS","RELIANCE.NS","ADANITRANS.BO","BAJAJ-AUTO.NS","GRASIM.BO","HINDALCO.NS","LT.NS","TITAN.NS","BRITANNIA.BO","DABUR.NS","YESBANK.BO","AXISBANK.NS","INDUSINDBK.BO","COALINDIA.NS","HIL.BO","BOSCHLTD.NS","DLF.BO","BIOCON.NS","CIPLA.NS","SIEMENS.BO","VEDL.BO"
#]

#stocks = ["SBIN.NS","TATAMTRDVR.BO","EICHERMOT.NS","MUTHOOTFIN.NS","PEL.NS"]
stocks = ["SBIN.NS"]
start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()
cl_price = pd.DataFrame()  # empty dataframe which will be filled with closing prices of each stock
ohlc_intraday = {}  # empty dictionary which will be filled with ohlcv dataframe for each ticker

a = yf.download("AMZN", start, end)

# looping over tickers and storing OHLCV dataframe in dictionary
for ticker in stocks:
    ohlc_intraday[ticker] = yf.download(ticker, start, end, interval='5m')
    del ohlc_intraday[ticker]["Close"]
    ohlc_intraday[ticker].columns=["Open","High","Low","Adj Close","Volume"]
    
tickers = ohlc_intraday.keys()



################################Backtesting####################################

#Merging renko df with original ohlc df
ohlc_renko = {}
df = copy.deepcopy(ohlc_intraday)
tickers_signal = {}
tickers_ret = {}
for ticker in tickers:
    print("merging for ",ticker)
    renko = renko_DF(df[ticker])
    renko.columns = ["Date","open","high","low","close","uptrend","bar_num"]
    df[ticker]["Date"] = df[ticker].index
    ohlc_renko[ticker] = df[ticker].merge(renko.loc[:,["Date","bar_num"]],how="outer",on="Date")
    ohlc_renko[ticker]["bar_num"].fillna(method='ffill',inplace=True)
    ohlc_renko[ticker]["macd"]= MACD(ohlc_renko[ticker],12,26,9)[0]
    ohlc_renko[ticker]["macd_sig"]= MACD(ohlc_renko[ticker],12,26,9)[1]
    ohlc_renko[ticker]["macd_slope"] = slope(ohlc_renko[ticker]["macd"],5)
    ohlc_renko[ticker]["macd_sig_slope"] = slope(ohlc_renko[ticker]["macd_sig"],5)
    tickers_signal[ticker] = ""
    tickers_ret[ticker] = []

   
#Identifying signals and calculating daily return
for ticker in tickers:
    print("calculating daily returns for ",ticker)
    for i in range(len(ohlc_intraday[ticker])):
        if tickers_signal[ticker] == "":
            tickers_ret[ticker].append(0)
            if i > 0:
                if ohlc_renko[ticker]["bar_num"][i]>=2 and ohlc_renko[ticker]["macd"][i]>ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]>ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = "Buy"
                elif ohlc_renko[ticker]["bar_num"][i]<=-2 and ohlc_renko[ticker]["macd"][i]<ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]<ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = "Sell"
        
        elif tickers_signal[ticker] == "Buy":
            tickers_ret[ticker].append((ohlc_renko[ticker]["Adj Close"][i]/ohlc_renko[ticker]["Adj Close"][i-1])-1)
            if i > 0:
                if ohlc_renko[ticker]["bar_num"][i]<=-2 and ohlc_renko[ticker]["macd"][i]<ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]<ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = "Sell"
                elif ohlc_renko[ticker]["macd"][i]<ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]<ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = ""
                
        elif tickers_signal[ticker] == "Sell":
            tickers_ret[ticker].append((ohlc_renko[ticker]["Adj Close"][i-1]/ohlc_renko[ticker]["Adj Close"][i])-1)
            if i > 0:
                if ohlc_renko[ticker]["bar_num"][i]>=2 and ohlc_renko[ticker]["macd"][i]>ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]>ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = "Buy"
                elif ohlc_renko[ticker]["macd"][i]>ohlc_renko[ticker]["macd_sig"][i] and ohlc_renko[ticker]["macd_slope"][i]>ohlc_renko[ticker]["macd_sig_slope"][i]:
                    tickers_signal[ticker] = ""
    ohlc_renko[ticker]["ret"] = np.array(tickers_ret[ticker])

#calculating overall strategy's KPIs
strategy_df = pd.DataFrame()
for ticker in tickers:
    strategy_df[ticker] = ohlc_renko[ticker]["ret"]
strategy_df["ret"] = strategy_df.mean(axis=1)
CAGR(strategy_df)
sharpe(strategy_df,0.025)
max_dd(strategy_df)  

#visualizing strategy returns
(1+strategy_df["ret"]).cumprod().plot()

#calculating individual stock's KPIs
cagr = {}
sharpe_ratios = {}
max_drawdown = {}
for ticker in tickers:
    print("calculating KPIs for ",ticker)      
    cagr[ticker] =  CAGR(ohlc_renko[ticker])
    sharpe_ratios[ticker] =  sharpe(ohlc_renko[ticker],0.025)
    max_drawdown[ticker] =  max_dd(ohlc_renko[ticker])

KPI_df = pd.DataFrame([cagr,sharpe_ratios,max_drawdown],index=["Return","Sharpe Ratio","Max Drawdown"])      
KPI_df=KPI_df.T

print(KPI_df)

# =============================================================================
# ORDER PLACING
# =============================================================================


cwd = os.chdir("D:\Developers Institute\DevelopersInstitute\Week7\Hackathon")

#generate trading session
access_token = open("access_token.txt",'r').read()
key_secret = open("api_key.txt",'r').read().split()
kite = KiteConnect(api_key=key_secret[0])
kite.set_access_token(access_token)

# while True:
#     for ticker in tickers:
#         print(f"checking buy condition for {ticker}")
#         if tickers_signal[ticker] == "Sell" and False:
#             tickers_ret[ticker].append(0)
#             if ohlc_renko[ticker]["bar_num"][-1]>=2 and ohlc_renko[ticker]["macd"][-1]>ohlc_renko[ticker]["macd_sig"][-1] and ohlc_renko[ticker]["macd_slope"][i]>ohlc_renko[ticker]["macd_sig_slope"][-1] and False:
#                 tickers_signal[ticker] = "Buy"
#                 company_name=ticker
#                 OrderPlace.placeMarketOrder(company_name,"buy",1)
#                 print(f"succesfully bought 1 share of {company_name}")
                
#         elif tickers_signal[ticker] == "Buy" and False:
#             tickers_ret[ticker].append((ohlc_renko[ticker]["Adj Close"][-1]/ohlc_renko[ticker]["Adj Close"][-2])-2)
#             if ohlc_renko[ticker]["bar_num"][-1]<=-2 and ohlc_renko[ticker]["macd"][-1]<ohlc_renko[ticker]["macd_sig"][-1] and ohlc_renko[ticker]["macd_slope"][-1]<ohlc_renko[ticker]["macd_sig_slope"][-1]:
#                 tickers_signal[ticker] = "Sell"
#                 company_name=ticker
#                 OrderPlace.placeMarketOrder(company_name,"sell",1)
#                 print(f"succesfully sold 1 share of {company_name}")
#         print(f"Buy condition for {ticker} failed, no purchase done, will check after 5 mins again")
#     time.sleep(900)
                
company_name="ACC"
OrderPlace.placeMarketOrder(company_name,"buy",1)
print(f"succesfully Bought 1 share of {company_name}")
    
# company_name="ACC"
# OrderPlace.placeMarketOrder(company_name,"sell",2)
# print(f"succesfully Sold 1 share of {company_name}")

