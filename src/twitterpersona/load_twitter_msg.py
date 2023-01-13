def load_twitter(input_file):
    """Load twitter dataset from a csv file and return as a dataframe.
    Parameters
    ----------
    input_file : str
        Path to text file.
    Returns
    -------
    dataframe
        dataframe contains all twitter info from dataset.
    Examples
    --------
    load_twitter("twitter.csv")
    """


def load_twitter_by_user(twitter_df, username):
    """Load dataframe which contains specific user from a complete twitter dataframe and return as a dataframe.
    Parameters
    ----------
    twitter_df : dataframe
        complete twitter dataframe.

    username : str
        specific username for twitter message.
    Returns
    -------
    dataframe
        dataframe contains username's twitter info from dataset.
    Examples
    --------
    load_twitter_by_user(twitter_df, 'andy')
    """



def load_twitter_by_id(twitter_df, user_id):
    """Load dataframe which contains specific userId from a complete twitter dataframe and return as a dataframe.
    Parameters
    ----------
    twitter_df : dataframe
        complete twitter dataframe.

    user_id : str
        specific userId for twitter message.
    Returns
    -------
    dataframe
        dataframe contains userId's twitter info from dataset.
    Examples
    --------
    load_twitter_by_id(twitter_df, '12345')
    """