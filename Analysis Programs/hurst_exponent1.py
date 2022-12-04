
import numpy as np
import matplotlib.pyplot as plt
from hurst import compute_Hc, random_walk
import seaborn as sns
import pandas as pd
import yfinance as yf
from sentiment_analysis import company_name 
import requests 

company_name = company_name

# send a GET request with the company name as keyword in the url
res = requests.get(
    f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={company_name}&apikey=')

ticker = res.json()

company = yf.Ticker(ticker)

company.info

company_df = yf.download(ticker,
                         start="2019-05-01",
                         end="2021-05-01",
                         progress=False)
company_df["Adj Close"].plot(title="Tesla")


def get_hurst_exponent(time_series, max_lag=20): 
    """Returns the Hurst Exponent of the time series"""

    lags = range(2, max_lag)

    # variances of the lagged differences
    tau = [np.std(np.subtract(time_series[lag:], time_series[:-lag]))
           for lag in lags]

    # calculate the slope of the log plot -> the Hurst Exponent
    reg = np.polyfit(np.log(lags), np.log(tau), 1)

    return reg[0]


for lag in [20, 100, 200, 300, 400]:
    hurst_exp = get_hurst_exponent(company_df["Adj Close"].values, lag)
    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")


for lag in [20, 100, 200, 300]:
    print(f"Hurst exponents with {lag} lags ----")
    for column in company.columns:
        print(
            f"{column}: {get_hurst_exponent(company_df[column].values, lag):.4f}")
