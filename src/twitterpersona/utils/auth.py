import tweepy

def authHandler():

    consumer_key = 'd2SlnFPCIkVAMTsF9GtBr3QXn'
    consumer_secret = 'amjTUjgDsrxlj7ZFeXt7249vUIrZtkKKYSKnxPEwMRqLdeNmnw'
    access_token = '1570310343091703808-KSFGDj2KZTGmJuaGXLwb8AYLqcIQt8'
    access_token_secret = 'xvKT1PPLkuA51l4pCZGEgMlNUythyR8AoW4xQq6DExCGV'
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    
    return api
