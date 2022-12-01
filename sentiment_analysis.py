import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize

# Company name for sentiment analysis
company_name = 'Tesla'

# Obtaining a reddit instance
reddit = praw.Reddit(
    client_id="9raDmXXDlTPfG8GW7x8EIA",
    client_secret="dLqBSSsGzwiizBROQWB2bRqty99qqw",
    password="",
    user_agent="web:stockmarketsentiment:v1 (by u/Organic-Drive4064",
    username="",
)


def get_reddit_data(subreddit):
    """
    Function to gather top submissions from a user specifed subreddit 
    Subreddit needs to be entered as a string 

    return: a list of submisssions 
    """
    list_submissions = []
    for submission in reddit.subreddit(subreddit).new(limit=None):
        if company_name in submission.title:
            list_submissions.append((submission.title, submission.selftext))

    return list_submissions


raw_data = get_reddit_data('StockMarket')



def clean_reddit_data():
    """
    Function to tokenize and 
    """
    string = ''.join(str(e) for e in raw_data)
    stop_list = set(stopwords.words('english'))
    word_tokens = word_tokenize(string)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_list]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_list:
            filtered_sentence.append(w)
    return filtered_sentence


clean_data = clean_reddit_data()
print(clean_data)


def convert_to_str(s):
    str1 = " "
    return str1.join(s)


clean_data_str = convert_to_str(clean_data)


def get_polarity():
    score = SIA().polarity_scores(clean_data_str)
    return score


score = get_polarity()

print(score)
