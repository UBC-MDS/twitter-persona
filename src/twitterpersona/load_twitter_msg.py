import pandas as pd
import tweepy
from utils.auth import authHandler # adding utils function for auth

def load_twitter_by_user(user, limit):
    """Load dataframe which contains specific user and return as a dataframe with total tweets.
    Parameters
    ----------
    user : str
        twitter user_name.

    limit : int
        how many tweets you wanna return.
    Returns
    -------
    dataframe
        dataframe contains username's twitter info.
    Examples
    --------
    load_twitter_by_user('Cristiano', 300)
    """
    api = authHandler()
    tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)
    # create DataFrame
    columns = ['User', 'Id', "created_at","favorite_count","retweet_count", "text" ]
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode("utf-8").decode("utf-8")])
        df = pd.DataFrame(data, columns=columns)
    return df



def load_twitter_by_keywords(key, limit):
    """Load dataframe which contains specific user and return as a dataframe with total tweets.
    Parameters
    ----------
    key : str
        tweets keyword.

    limit : int
        how many tweets you wanna return.
    Returns
    -------
    dataframe
        dataframe contains username's twitter info.
    Examples
    --------
    load_twitter_by_keywords('2022', 100)
    """
    api = authHandler()
    tweets = tweepy.Cursor(api.search_tweets, q=key, count=100, tweet_mode='extended').items(limit)
    # create DataFrame
    columns = ['User', 'Id', "created_at","favorite_count","retweet_count", "text" ]
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode("utf-8").decode("utf-8")])
        df = pd.DataFrame(data, columns=columns)
    return df