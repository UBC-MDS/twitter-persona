def get_sentiment_result(df, sentiment):
    """get Negative, Positive, or Neutral twitters from processed dataframe.
    Parameters
    ----------
    df : pd.DataFrame
        dataframe after pre-processing
    
    sentiment : str
        string represent positive, negative or neutral sentiment
    
    Returns
    -------
    dataframe
        dataframe contains all tweets info for a specific sentiment.
    Examples
    --------
    get_sentiment_result(df, 'positive')
    """


def count_tweets(df):
    """count how many tweets in each sentiment dataframe
    Parameters
    ----------
    df : pd.DataFrame
        dataframe for each sentiment
    
    Returns
    -------
    dataframe
        dataframe contains number of tweets for each sentiment dataframe
    Examples
    --------
    count_tweets(df)
    """