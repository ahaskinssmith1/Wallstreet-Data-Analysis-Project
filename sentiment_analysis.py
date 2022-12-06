import praw
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize
from api_keys import client_id, client_secret


# Import Reddit client information
client_id = client_id

client_secret = client_secret


# Obtaining a reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    password="",
    user_agent="web:stockmarketsentiment:v1 (by u/Organic-Drive4064",
    username="",
)


def get_reddit_data(subreddit, company_name):
    """
    Function to gather top submissions from a user specifed subreddit 
    Subreddit needs to be entered as a string 

    return: a list of subreddit submisssions 
    """
    list_submissions = []
    for submission in reddit.subreddit(subreddit).new(limit=None):
        if company_name in submission.title:
            list_submissions.append(submission.title)
            list_submissions.append(submission.selftext)

    return list_submissions


def clean_reddit_data(data):
    """
    Function to tokenize text and remove any tokens that are included in the NLTK stopwords set 

    return: a list of words from company related subreddit submissions 
    """
    string = ''.join(str(e) for e in data)
    stop_list = set(stopwords.words('english'))
    word_tokens = word_tokenize(string)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_list]
    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_list:
            filtered_sentence.append(w)
    return filtered_sentence


def convert_to_str(s):
    """
    Function to convert a list into a string for the sentiment intensity analyzer 

    return: a string 
    """
    str1 = " "
    return str1.join(s)


def get_polarity(str):
    """
    Function to obtain a polarity score for a string 

    return: a dictionary containing polarity coefficents
    """
    score = SIA().polarity_scores(str)
    return score


def interpret_polarity(company_name):
    """
    Function to interprete the compound polarity output 

    return: a string describing valence of subreddit sumbmissions which mention the company name 
    """
    print('starting interpret_polarity function...')
    print(f'Now checking {company_name} on reddit')
    raw_data = get_reddit_data("StockMarket", company_name)
    clean_data = clean_reddit_data(raw_data)
    clean_data_str = convert_to_str(clean_data)
    polarity = get_polarity(clean_data_str)
    compound = polarity.get('compound')

    if compound <= 0:
        return f'The compound score is {compound} which indicates a negative valence related to {company_name}'
    else:
        return f'The compound score is {compound} which indicates a positive valence related to {company_name}'


def main():
    output = interpret_polarity("Tesla")
    print(output)


if __name__ == "__main__":
    main()
