from twitterpersona.generate_word_cloud import create_wordcloud, set_colourmap, transform_zeros
import pytest
import pandas as pd
import matplotlib

# Define supporting functions

@pytest.fixture
def neg_input_df():
    """Define a pd.DataFrame containing mainly negative tweets by one user."""
    neg_input = pd.DataFrame({
        "User": {"0": "Renzo", "1": "Renzo", "2": "Renzo", "3": "Renzo"},
        "text": {
            "0": "I hate this place, I think everyone here is very rude!",
            "1": "I\'ve never enjoyed something as simple and mundane as this game.",
            "2": "Very often I just can\'t see the fun in something when other people do, it\'s like I just don\'t know how to have fun.",
            "3": "I don\'t think this administration has accomplished anything noteworthy in the two years they\'ve been in power. It\'s a disgrace!"
        }, 
        "text_clean": {
            "0": "I hate place, I think everyone rude!",
            "1": "I\'ve never enjoyed something simple mundane game.",
            "2": "Very often I can\'t see fun something people do, like I know fun.",
            "3": "I think administration accomplished anything noteworthy two years they\'ve power. It\'s disgrace!"
        }, 
        "sentiment": {
            "0": "negative",
            "1": "negative",
            "2": "negative",
            "3": "negative"
        }
    })
    return neg_input

@pytest.fixture
def pos_input_df():
    """Define a pd.DataFrame containing mainly positive tweets by one user."""
    pos_input = pd.DataFrame({
        "User": {"0": "Timmy", "1": "Timmy", "2": "Timmy", "3": "Timmy"},
        "text": {
            "0": "I absolutely love it here! I think moving here was one of the best decisions of my life.",
            "1": "This is an incredibly exciting game and I recommend that everyone who likes this genre gives it a go!",
            "2": "I went out with my firends last night: we het the town, had some drinks, and ended up doing karaoke! Such a good time",
            "3": "I received a really good grade for my python package! I\'m so happy!"
        }, 
        "text_clean": {
            "0": "I absolutely love here! I think moving one best decisions life.",
            "1": "This incredibly exciting game I recommend everyone likes genre gives go!",
            "2": "I went firends last night: het town, drinks, ended karaoke! Such good time",
            "3": "I received really good grade python package! I\'m happy!"
        }, 
        "sentiment": {
            "0": "positive",
            "1": "positive",
            "2": "positive",
            "3": "positive"
        }
    })
    return pos_input

# Tests

def test_fig_size(neg_input_df):
    """Test whether the output image is the correct size."""
    wordcloud = create_wordcloud(neg_input_df)
    assert wordcloud.get_figheight() == 8.0


def test_fig_type(neg_input_df):
    """Test whether type of output is correct."""
    wordcloud = create_wordcloud(neg_input_df)
    assert type(wordcloud) is matplotlib.figure.Figure


def test_neg_colour(neg_input_df):
    """Test whether the correct colourmap is being applied for negative Tweets."""
    colourmap = set_colourmap(neg_input_df)
    assert colourmap == 'autumn'


def test_pos_colour(pos_input_df):
    """Test whether the correct colourmap is being applied for positive Tweets."""
    colourmap = set_colourmap(pos_input_df)
    assert colourmap == 'summer'


def test_transform_zeros_zero():
    """Test whether the transform function is working correctly when fed 0."""
    val = transform_zeros(0)
    assert val == 255


def test_transform_zeros_val():
    """Test whether the transform function is working correctly when fed !0."""
    val = transform_zeros(524)
    assert val == 524
