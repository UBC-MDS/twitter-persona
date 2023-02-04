from twitterpersona.sentiment_analysis import sentiment_labler, count_tweets
import pytest
import pandas as pd

# Define supporting functions

@pytest.fixture
def input_df():
    input_df = pd.DataFrame({
        'User': {20: 'POTUS', 21: 'POTUS', 22: 'POTUS', 23: 'POTUS', 24: 'POTUS', 25: 'POTUS', 26: 'POTUS', 27: 'POTUS'},
        'text': {
            20: 'In America, we go forward when we go together.',
            21: "Like Dr. King, I know that there is nothing beyond this nation's capacity. \n\nWe will fulfill the promise of America for all Americans. https://t.co/toXTEOtIVj",
            22: "Let us be guided by Dr. King's light today. And by the charge of Scripture:\n\n“Let us never grow weary in doing what is right – for if we do not give up we will reap our harvest in due time.”",
            23: "My Administration laid the foundation for a stronger, more resilient, and more equitable economy for decades to come.\n\nTwo years in – it's clear our economic plan is working. https://t.co/OtfL4abi2j",
            24: 'This is a time for choosing. \n\nWill we choose democracy over autocracy?\nCommunity over chaos?\nLove over hate?\n\nThese are questions of our time that I ran for president to help answer. And of which Dr. King’s life and legacy will guide us forward.',
            25: 'Tune in as I deliver remarks at the National Action Network Martin Luther King, Jr. Day Breakfast. https://t.co/q6IH0MDAvk',
            26: 'In the Oval Office is a bust of Dr. King.\n \nI often think of the question Dr. King asked us all those years ago: “where do we go from here?”\n \nMy message today is that we go forward when we go together.',
            27: 'Today, we honor the Reverend Dr. Martin Luther King, Jr. by continuing his unfinished work to redeem the soul of America. https://t.co/yJ4rmLyJyt'
        }
    })
    return input_df

# Tests

def test_df_shape(input_df):
    """Test expected output shape of output."""
    labeled_df = sentiment_labler(input_df, 'text')
    assert labeled_df.shape == (8, 3)

def test_sentiment_col(input_df):
    """Check for sentiment column in output."""
    labeled_df = sentiment_labler(input_df, 'text')
    assert "sentiment" in labeled_df.columns

def test_labels(input_df):
    """Test for all three different types of sentiment."""
    labeled_df = sentiment_labler(input_df, 'text')
    assert len(labeled_df["sentiment"].unique()) == 3

def test_dict(input_df):
    """Test whether type of output is correct."""
    labeled_df = sentiment_labler(input_df, 'text')
    count_dict = count_tweets(labeled_df)
    assert type(count_dict) == dict

def test_props(input_df):
    """Check whether the sentiment analysis proportion is correct."""
    labeled_df = sentiment_labler(input_df, 'text')
    count_dict = count_tweets(labeled_df)
    assert count_dict == {'positive': 0.5, 'neutral': 0.375, 'negative': 0.125}

def test_count(input_df):
    """Check whether the sentiment analysis numbers are correct."""
    labeled_df = sentiment_labler(input_df, 'text')
    count_dict = count_tweets(labeled_df, proportion=False)
    assert count_dict == {'positive': 4, 'neutral': 3, 'negative': 1}