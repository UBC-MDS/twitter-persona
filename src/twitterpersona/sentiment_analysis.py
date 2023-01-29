import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

nltk.download("vader_lexicon")

def sentiment_labler(df, col):
    """
    Labelling each row in a given column of tweets/text with positive, negative or neutral sentiment.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe that has been pre-processed.
    
    col : str
        Column name of the column containing tweets in the dataset.
    
    Returns
    -------

    df : pd.DataFrame
        Dataframe contains all tweets the corresponding labels.

    Examples
    --------
    sentiment_labler(df, "text")
    """
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


def count_tweets(df, proportion= True):
    """
    Count the proportion of different sentiment tweets in a labelled sentiment dataframe

    Parameters
    ----------
    df : pd.DataFrame
        dataframe for each sentiment
    
    proportion : bool
        if True: returns the proportion; otherwise, return the counts.
    
    Returns
    -------
    dictionary
        A dictionary which calculates the proportion of three sentiments of tweets.

    Examples
    --------
    labelled_df = sentiment_labler(df, "text")
    count_tweets(labelled_df)
    """

    if proportion:
        sentiment_counts = df['sentiment'].value_counts(normalize = True)
    else:
        sentiment_counts = df['sentiment'].value_counts()

    return dict(sentiment_counts)


    