def sentiment_labler(df, col):
    """labelling each row in a given column of tweets/text with positive, negative or neutral sentiment
    Parameters
    ----------
    df : pd.DataFrame
        dataframe after pre-processing
    
    col : str
        column name of the tweets in the dataset
    
    Returns
    -------
    dataframe
        dataframe contains all tweets the corresponding labels
    Examples
    --------
    get_sentiment_result(df, "text")
    """
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()

    def extract_sentiment(text):
        #Only three labels used by NLTK sentiment analyzer: neutral, positive and negative
        #each with a score
        #The sentiment is calculated based on the compound score with thresholds explained in:
        #https://towardsdatascience.com/social-media-sentiment-analysis-in-python-with-vader-no-training-required-4bc6a21e87b8
        scores = sid.polarity_scores(text)
        if scores["compound"] > 0.05:
            return "positive"
        elif scores["compound"] < -0.05:
            return "negative"
        else:
            return "neutral"

    labelled_df = df.assign(sentiment=df[col].apply(extract_sentiment))
    return labelled_df


def count_tweets(df):
    """count how propotion of tweets in each sentiment dataframe
    Parameters
    ----------
    df : pd.DataFrame
        dataframe for each sentiment
    
    Returns
    -------
    dicitionary
        a dicionary contains the proportion of three sentiment of tweets
    Examples
    --------
    count_tweets(df)
    """