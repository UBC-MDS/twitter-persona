import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from twitterpersona.sentiment_analysis import count_tweets
import urllib.request

def transform_zeros(val):
    """
    Helper function to correct the mask array.

    Parameters
    ----------
    val : int
        Any integer.
    
    Returns
    -------
    val : int
        255 if val is 0, and val otherwise.

    Examples
    --------
    transform_zeros(0)
    """

    if val == 0: 
       return 255
    else:
       return val

def set_colourmap(df):
    """
    Determine the corresponding colourmap for a certain users
    tweet sentiment analysis.

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
    set_colourmap(df)
    """

    # Determine tweet sentiment
    sentiment = count_tweets(df)

    # Set wordcloud colour
    if max(sentiment, key=sentiment.get) == 'positive':
        return('summer')
    elif max(sentiment, key=sentiment.get) == 'negative':
        return('autumn')
    else:
        return('cool')

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

    # Import image from URL
    URL = 'https://www.edigitalagency.com.au/wp-content/uploads/twitter-logo-black-png.png'

    with urllib.request.urlopen(URL) as url:
        img = Image.open(url)
        mask = np.array(img)

    # Transform image to usable mask
    maskable_image = np.ndarray((mask.shape[0],mask.shape[1]), np.int32)
    for i in range(len(mask)):
        maskable_image[i] = list(map(transform_zeros, mask[i]))
    mask = maskable_image

    # Combine all tweets into single string
    text = " ".join(tweet for tweet in df["text_clean"])

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
        colormap = set_colourmap(df)
    ).generate(text)
    fig = plt.figure(figsize = (8, 8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad = 0)
    plt.show()
    
    return fig
