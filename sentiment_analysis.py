import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA 
import nltk 
import requests 
import urllib.request
reddit = praw.Reddit(
    client_id="9raDmXXDlTPfG8GW7x8EIA",
    client_secret="dLqBSSsGzwiizBROQWB2bRqty99qqw",
    password="",
    user_agent="web:stockmarketsentiment:v1 (by u/Organic-Drive4064",
    username="",
)


print(reddit.read_only)


#for submission in reddit.subreddit("StockMarket").new(limit = None): 
    #print(submission.title)





def get_reddit_data(subreddit): 
    """
    Function to gather top submissions from a user specifed subreddit 
    Subreddit needs to be entered as a string 
    """
    for submission in reddit.subreddit(subreddit).new(limit = 20):
        url = 'https://www.reddit.com'+ submission.permalink + '.json'
        with urllib.request.urlopen(url) as f:
            response = urllib.request.urlopen(url)
            data = response.read() 
            print(data)

get_reddit_data('StockMarket')






    




