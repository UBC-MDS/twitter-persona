def get_top_n_word(df, n):
    """get top n words from a specific sentiment dataframe.
    Parameters
    ----------
    df : pd.DataFrame
        dataframe after sentiment_analysis
    
    n : int
        how many number of top existing words in dataframe with tweets msg column
    
    Returns
    -------
    dict : dictionary
        dictionary with key as word that has highest frequency and value as how many number it show up
    Examples
    --------
    get_top_n_word(df, 5)
    """

def create_wordcloud(text, output_path):
    """Create Wordcloud.
    Parameters
    ----------
    text : str
        tweets message
    
     output_path : str
        the path that the newly generated png should located at
    
    Returns
    -------
    wordcount : png
        the picture of wordcount
    Examples
    --------
    create_wordcloud('today is bad day', /output)
    """