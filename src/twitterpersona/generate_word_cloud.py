import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from twitterpersona.sentiment_analysis import count_tweets

def create_wordcloud(df):
    """
    Create a wordcloud out of all the tweets of a user. 
    Wordcloud colour is green if the overal sentiment of the
    users tweets is positive, red if negative and blue if 
    neutral.

    Parameters
    ----------
    df : pd.DataFrame
        A dataframe with all the tweets of a user, and their
        sentiment analysis.
    
    Returns
    -------
    plot : plt.figure()
        A matplotlib plot of the wordcloud.
    
    Examples
    --------
    create_wordcloud(df)
    """

    # Import image to np.array
    url = "https://raw.githubusercontent.com/UBC-MDS/twitter-persona/30d12d4ff486995feb9416672b6b278b969b301d/src/twitterpersona/twitterLogo.png"
    #mask = np.array(Image.open('twitterLogo.png'))
    mask = Image.open(requests.get(url, stream=True).raw)
    
    # Combine all tweets into single string
    text = " ".join(tweet for tweet in df["text_clean"])

    # Determine tweet sentiment
    sentiment = count_tweets(df)

    # Set wordcloud colour
    if sentiment.idxmax() == 'positive':
        colormap = 'summer'
    elif sentiment.idxmax() == 'negative':
        colormap = 'autumn'
    else:
        colormap = 'cool'

    # Create the wordcloud
    wordcloud = WordCloud(
        width = 800, 
        height = 800, 
        min_font_size = 10, 
        stopwords = STOPWORDS,
        mask = mask,
        background_color = 'white',
        contour_color = '#00aced',
        contour_width = 8,
        colormap = colormap
    ).generate(text)
    fig = plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    
    return fig
