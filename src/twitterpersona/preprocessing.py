import pandas as pd
import preprocessor as p
import nltk
from nltk.corpus import stopwords


def generalPreprocessing(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Perform general preprocessing on df. Removes retweets/favourites and cleans URLs, Mentions, Numbers, and stop words.  
    
    Parameters
    ----------
    df : pd.DataFrame
        dataframe storing all the raw data with text column
    
    output_path : str
        the path that the newly generated csv should located at
    
    Returns
    -------
    df : pd.DataFrame
        processed tweet dataframe.
        
    Examples
    --------
    generalPreprocessing(df)
    '''

    # remove retweets/favourites
    rt_fav_pattern = r'\b(RT|FAV)\b'
    filter = df['text'].str.contains(rt_fav_pattern, regex=True)
    df = df[~filter]

    # remove URL, Mentions, and Numbers
    p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.NUMBER)
    df['text_clean'] = df['text'].apply(lambda x: p.clean(x))

    # remove rows withstop words
    nltk.download('stopwords')
    df['text_clean'] = df['text_clean'].apply(lambda x: ' '.join([word for word in x.split() if word not in stopwords.words('english')]))

    return df
