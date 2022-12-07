
# Wallstreet Data Analysis :chart_with_upwards_trend:


The Wallstreet Data Analysis project is for anyone who is looking for a convenient and very easy-to-use resource for gaining deeper insight into public opinions and market regimes for a publicly traded company. 


# How to run it? :running:

1. Access our code using the following https://github.com/ahaskinssmith1/Wallstreet-Data-Analysis-Project
2. Download all the required packages listed below using the Command Prompt (pip install <package name>)
3. run the app.py and follow the website link which will be given as an output
4. Input the necessary information into the search bar on the Wall Street Data website (company name & ticker)

# Packages :file_folder:

**Required packages for the app.py**

from flask import Flask, render_template, request, redirect 

from sentiment_analysis import interpret_polarity

from hurst_exponent1 import interpret_hurst

**Required packages for the hurst_exponent.py**

import numpy as np

import matplotlib.pyplot as plt

from hurst import compute_Hc, random_walk

import seaborn as sns

import pandas as pd

import yfinance as yf

**Required packages for the sentiment_analysis.py** 

praw

nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
## API Reference

#### Get keys

```http
  https://praw.readthedocs.io/en/stable/getting_started/authentication.html
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `client_secret` | `string` | **Required**. Your API key |
| `client_id` | `string` | **Required**. Your authorization key (OAuth 2.0); |

The OAuth 2.0 authorization framework enables a third-party
   application to obtain limited access to an HTTP service, either on
   behalf of a resource owner by orchestrating an approval interaction
   between the resource owner and the HTTP service, or by allowing the
   third-party application to obtain access on its own behalf.





