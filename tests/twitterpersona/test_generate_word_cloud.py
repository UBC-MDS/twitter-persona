from twitterpersona.generate_word_cloud import create_wordcloud
import pytest
import pandas as pd

@pytest.fixture
def neg_input_df():
    input = pd.DataFrame({'User': {0: 'Renzo', 1: 'Renzo', 2: 'Renzo', 3: 'Renzo'},
                  'text': {0: 'I hate this place, I think everyone here is very rude!',
                            1: "I've never enjoyed something as simple and mundane as this game.",
                            2: "Very often I just can't see the fun in something when other people do, it's like I just don't know how to have fun.",
                            3: "I don't think this administration has accomplished anything noteworthy in the two years they've been in power. It's a disgrace!",
                            }})
    return input

@pytest.fixture
def pos_input_df():
    input = pd.DataFrame({'User': {0: 'Timmy', 1: 'Timmy', 2: 'Timmy', 3: 'Timmy'},
                  'text': {0: 'I absolutely love it here! I think moving here was one of the best decisions of my life.',
                            1: "This is an incredibly exciting game and I recommend that everyone who likes this genre gives it a go!",
                            2: "I went out with my firends last night: we het the town, had some drinks, and ended up doing karaoke! Such a good time",
                            3: "I received a really good grade for my python package! I'm so happy!"
                            }})
    return input

def text_colour(neg_input_df):
    wordcloud = create_wordcloud(neg_input_df)
    assert wordcloud.get_figheight == 800

def text_colour(neg_input_df):
    wordcloud = create_wordcloud(neg_input_df)
    assert wordcloud.colormap == 'autumn'

def text_colour(pos_input_df):
    wordcloud = create_wordcloud(pos_input_df)
    assert wordcloud.colormap == 'summer'