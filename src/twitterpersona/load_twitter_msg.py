import pandas as pd
import tweepy
#from utils.auth import authHandler # adding utils function for auth


def user_info(consumer_key_input, consumer_secret_input, access_token_input, access_token_secret_input):
    """Take four input parameters with user credentials and stored in a list object.
    Parameters
    ----------
    consumer_key_input : str
        twitter consumer key.

    consumer_secret_input : str
        twitter consumer secret.

    access_token_input  : str
        twitter token.

    access_token_secret_input : str
        twitter token secret.
    
    Returns
    -------
    user_info : list 
        list contains above user info.
    Examples
    --------
    user_info('consumer_key_input', 'consumer_secret_input', 'access_token_input', 'access_token_secret_input')
    """
    user_info = {
    "consumer_key": consumer_key_input,
    "consumer_secret": consumer_secret_input,
    "access_token": access_token_input,
    "access_token_secret": access_token_secret_input
    }

    return user_info

def load_twitter_by_user(user, limit, user_info):
    """Load dataframe which contains specific user and return as a dataframe with total tweets.
    Parameters
    ----------
    user : str
        Twitter user_name.

    limit : int
        How many tweets you wanna return.

    Returns
    -------
    pd.DataFrame : 
        Dataframe contains username's twitter info.

    Examples
    --------
    load_twitter_by_user('Cristiano', 300)
    """
    consumer_key = user_info['consumer_key']
    consumer_secret = user_info['consumer_secret']
    access_token = user_info['access_token']
    access_token_secret = user_info['access_token_secret']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

    # create DataFrame
    columns = ['User', 'Id', "created_at","favorite_count","retweet_count", "text" ]
    data = []

    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode("utf-8").decode("utf-8")])
        df = pd.DataFrame(data, columns=columns)

    return df


def load_twitter_by_keywords(key, limit, user_info):
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
    consumer_key = user_info['consumer_key']
    consumer_secret = user_info['consumer_secret']
    access_token = user_info['access_token']
    access_token_secret = user_info['access_token_secret']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    tweets = tweepy.Cursor(api.search_tweets, q=key, count=100, tweet_mode='extended').items(limit)

    # create DataFrame
    columns = ['User', 'Id', "created_at","favorite_count","retweet_count", "text" ]
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.id_str, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text.encode("utf-8").decode("utf-8")])
        df = pd.DataFrame(data, columns=columns)
        
    return df