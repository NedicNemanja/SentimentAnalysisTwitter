
def remove_chars(tweets,chars):
    for tweet in tweets:
        tweet[1] = ''.join( c for c in tweet[1] if  c not in chars )
    return tweets
