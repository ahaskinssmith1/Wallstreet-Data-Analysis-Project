# %%
pip install hurst

# %%
import numpy as np 

# %%
import matplotlib.pyplot as plt 

# %%
from hurst import compute_Hc, random_walk 

# %%
import seaborn as sns 

# %%
import pandas as pd

# %%
pip install yfinance

# %%
import yfinance as yf

# %%
tsla = yf.Ticker("TSLA")

# %%
tsla.info

# %%
tsla_df = yf.download("TSLA", 
                     start="2019-05-01", 
                     end="2021-05-01", 
                     progress=False)
tsla_df["Adj Close"].plot(title="Tesla");

# %%
def get_hurst_exponent(time_series, max_lag=20):
    """Returns the Hurst Exponent of the time series"""
    
    lags = range(2, max_lag)

    # variances of the lagged differences
    tau = [np.std(np.subtract(time_series[lag:], time_series[:-lag])) for lag in lags]

    # calculate the slope of the log plot -> the Hurst Exponent
    reg = np.polyfit(np.log(lags), np.log(tau), 1)

    return reg[0]

# %%
for lag in [20,100,200,300,400]:
    hurst_exp = get_hurst_exponent(tsla_df["Adj Close"].values, lag)
    print(f"Hurst exponent with {lag} lags: {hurst_exp:.4f}")

# %%
for lag in [20, 100, 200,300 ]:
    print(f"Hurst exponents with {lag} lags ----")
    for column in tsla_df.columns:
        print(f"{column}: {get_hurst_exponent(tsla_df[column].values, lag):.4f}")

# %%



