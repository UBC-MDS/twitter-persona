from twitterpersona.preprocessing import generalPreprocessing
import pytest
import pandas as pd

@pytest.fixture
def potus_df():
    """create fixutre potus_df with POTUS df"""
    input = pd.DataFrame({'User': {20: 'POTUS', 21: 'POTUS', 22: 'POTUS', 23: 'POTUS', 24: 'POTUS', 25: 'POTUS', 26: 'POTUS', 27: 'POTUS'},
                  'text': {20: 'In America, we go forward when we go together.',
                            21: "Like Dr. King, I know that there is nothing beyond this nation's capacity. \n\nWe will fulfill the promise of America for all Americans. https://t.co/toXTEOtIVj",
                            22: "Let us be guided by Dr. King's light today. And by the charge of Scripture:\n\n“Let us never grow weary in doing what is right – for if we do not give up we will reap our harvest in due time.”",
                            23: "My Administration laid the foundation for a stronger, more resilient, and more equitable economy for decades to come.\n\nTwo years in – it's clear our economic plan is working. https://t.co/OtfL4abi2j",
                            24: 'This is a time for choosing. \n\nWill we choose democracy over autocracy?\nCommunity over chaos?\nLove over hate?\n\nThese are questions of our time that I ran for president to help answer. And of which Dr. King’s life and legacy will guide us forward.',
                            25: 'Tune in as I deliver remarks at the National Action Network Martin Luther King, Jr. Day Breakfast. https://t.co/q6IH0MDAvk',
                            26: 'In the Oval Office is a bust of Dr. King.\n \nI often think of the question Dr. King asked us all those years ago: “where do we go from here?”\n \nMy message today is that we go forward when we go together.',
                            27: 'Today, we honor the Reverend Dr. Martin Luther King, Jr. by continuing his unfinished work to redeem the soul of America. https://t.co/yJ4rmLyJyt'
                            }})
    return input

@pytest.fixture
def RT_FAV_input_df():
    """create fixutre RT_FAV_input_df with sample data"""
    df = pd.DataFrame({'User': {1: 'POTUS', 2: 'POTUS', 3: 'POTUS'},
                  'text': {1: 'RT tweet gets removed',
                            2: 'FAV tweet gets removed',
                            3: 'tweet passes'
                            }})
    return df

@pytest.fixture
def url_mention_number_input_df():
    """create fixutre url_mention_number_input_df with sample data"""
    df = pd.DataFrame({'User': {1: 'POTUS', 2: 'POTUS', 3: 'POTUS', 3: 'POTUS'},
                  'text': {1: 'tweet url https://t.co/q6IH0MDAvk',
                            2: 'tweet @POTUS mention',
                            3: 'tweet numbers 12345',
                            4: 'tweet https://t.co/yJ4rmLyJyt 8234 @mention, url, number'
                            }})
    return df

@pytest.fixture
def stop_words_input_df():
    """create fixutre stop_words_input_df with sample data"""
    df = pd.DataFrame({'User': {1: 'POTUS', 2: 'POTUS', 3: 'POTUS', 3: 'POTUS'},
                  'text': {1: 'tweet with stop words',
                            2: 'tweet having a stop word and two more',
                            3: 'tweet without stop words',
                            4: 'he had no time to do it by himself so he got help from others'
                            }})
    return df

def test_RT_FAV_remove(RT_FAV_input_df):
    """Test the removal of rows that are Retweets or Favourites"""
    clean_df = generalPreprocessing(RT_FAV_input_df)
    df_exp = pd.DataFrame({ 'User': {3: 'POTUS'},
                            'text': {3: 'tweet passes'},
                            'text_clean': {3: 'tweet passes'}
                            })
    assert clean_df.equals(df_exp)

def test_url_mention_number_remove(url_mention_number_input_df):
    """Test the removal of urls, mentions, and numbers from tweet text"""
    clean_df = generalPreprocessing(url_mention_number_input_df)
    df_exp = pd.DataFrame({'User': {1: 'POTUS', 2: 'POTUS', 3: 'POTUS'},
                            'text': {1: 'tweet url https://t.co/q6IH0MDAvk',
                                    2: 'tweet @POTUS mention',
                                    3: 'tweet numbers 12345',
                                    4: 'tweet https://t.co/yJ4rmLyJyt 8234 @mention, url, number'
                                    },
                            'text_clean':{1: 'tweet url',
                                    2: 'tweet mention',
                                    3: 'tweet numbers',
                                    4: 'tweet , url, number'

                            }})
    assert clean_df.equals(df_exp)

def test_stop_words_remove(stop_words_input_df):
    """test the removal of nltk stopwords from tweet text"""
    clean_df = generalPreprocessing(stop_words_input_df)
    df_exp = pd.DataFrame({'User': {1: 'POTUS', 2: 'POTUS', 3: 'POTUS', 3: 'POTUS'},
                  'text': {1: 'tweet with stop words',
                            2: 'tweet having a stop word and two more',
                            3: 'tweet without stop words',
                            4: 'he had no time to do it by himself so he got help from others'
                            },
                            'text_clean':{1: 'tweet stop words',
                                            2: 'tweet stop word two',
                                            3: 'tweet without stop words',
                                            4: 'time got help others'
                            }})
    assert clean_df.equals(df_exp)

def test_df_shape(potus_df):
    """tedt expected output shape"""
    clean_df = generalPreprocessing(potus_df)
    assert clean_df.shape == (8, 3)

def test_text_clean_col(potus_df):
    """Check for text_clean column in output df"""
    clean_df = generalPreprocessing(potus_df)
    assert "text_clean" in clean_df.columns

def test_potus_df(potus_df):
    """Test function on sample real twitter data from @POTUS"""
    clean_df = generalPreprocessing(potus_df)
    df_exp = pd.DataFrame({  'User': {20: 'POTUS', 21: 'POTUS', 22: 'POTUS', 23: 'POTUS', 24: 'POTUS', 25: 'POTUS', 26: 'POTUS', 27: 'POTUS'},
                'text': {   20: 'In America, we go forward when we go together.',
                            21: "Like Dr. King, I know that there is nothing beyond this nation's capacity. \n\nWe will fulfill the promise of America for all Americans. https://t.co/toXTEOtIVj",
                            22: "Let us be guided by Dr. King's light today. And by the charge of Scripture:\n\n“Let us never grow weary in doing what is right – for if we do not give up we will reap our harvest in due time.”",
                            23: "My Administration laid the foundation for a stronger, more resilient, and more equitable economy for decades to come.\n\nTwo years in – it's clear our economic plan is working. https://t.co/OtfL4abi2j",
                            24: 'This is a time for choosing. \n\nWill we choose democracy over autocracy?\nCommunity over chaos?\nLove over hate?\n\nThese are questions of our time that I ran for president to help answer. And of which Dr. King’s life and legacy will guide us forward.',
                            25: 'Tune in as I deliver remarks at the National Action Network Martin Luther King, Jr. Day Breakfast. https://t.co/q6IH0MDAvk', 26: 'In the Oval Office is a bust of Dr. King.\n \nI often think of the question Dr. King asked us all those years ago: “where do we go from here?”\n \nMy message today is that we go forward when we go together.',
                            27: 'Today, we honor the Reverend Dr. Martin Luther King, Jr. by continuing his unfinished work to redeem the soul of America. https://t.co/yJ4rmLyJyt'
                        },
                'text_clean': { 20: 'In America, go forward go together.',
                                21: "Like Dr. King, I know nothing beyond nation's capacity. We fulfill promise America Americans.",
                                22: "Let us guided Dr. King's light today. And charge Scripture: “Let us never grow weary right – give reap harvest due time.”",
                                23: 'My Administration laid foundation stronger, resilient, equitable economy decades come. Two years – clear economic plan working.',
                                24: 'This time choosing. Will choose democracy autocracy? Community chaos? Love hate? These questions time I ran president help answer. And Dr. King’s life legacy guide us forward.',
                                25: 'Tune I deliver remarks National Action Network Martin Luther King, Jr. Day Breakfast.',
                                26: 'In Oval Office bust Dr. King. I often think question Dr. King asked us years ago: “where go here?” My message today go forward go together.',
                                27: 'Today, honor Reverend Dr. Martin Luther King, Jr. continuing unfinished work redeem soul America.'
                                }
            })
    assert clean_df.equals(df_exp)
    