def generalPreprocessing(df, output_path):
    '''
    Perform general preprocessing on df
    
    Parameters
    ----------
    df : pd.DataFrame
        dataframe storing all the raw data with text column
    
    output_path : str
        the path that the newly generated csv should located at
    
    Returns
    -------
    df : pd.DataFrame
        preprocessed (fix type, drop unused column, arrange column order, add text column) dataframe and export as a csv file.
        
    Examples
    --------
    generalPreprocessing(df)
    df object
    '''

def clean_punctuation(tweets):
    '''
    clean all punctuations and special mark for each twitter message(s)
    
    Parameters
    ----------
    tweets : str
        tweets message for each twitter
    
    Returns
    -------
    tweets : str
         tweets contains non-punctuations and special marks string message
        
    Examples
    --------
    clean_punctuation('Today is a good day!')
    tweets str
    '''

def extract_emojis(df):
    '''
    extract a list containing the emojis in the tweet
    
    Parameters
    ----------
    df : pd.DataFrame
        dataframe storing all the raw data with text column
    
    Returns
    -------
    lst: list
        list of Emojis tweets
        
    Examples
    --------
    extract_emojis(df)
    '''

