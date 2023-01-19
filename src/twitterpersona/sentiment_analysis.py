def sentiment_labler(df):
    """labelling each tweet a given twitter dataframe with positive, negative or neutral sentiment
    Parameters
    ----------
    df : pd.DataFrame or pd.Series
        dataframe after pre-processing
    
    Returns
    -------
    dataframe
        dataframe contains all tweets the corresponding labels
    Examples
    --------
    get_sentiment_result(df)
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()


def count_tweets(df):
    """count how propotion of tweets in each sentiment dataframe
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