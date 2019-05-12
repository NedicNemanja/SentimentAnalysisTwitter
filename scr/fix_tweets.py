
def remove_chars(tweet,chars):
        tweet = ''.join( c for c in tweet if  c not in chars )
        return tweet

#source:https://gist.github.com/gruber/8891611
def remove_links(tweet):
    import re
    import urlmarker
    links=re.findall(urlmarker.URL_REGEX, tweet)
    for link in links:
        tweet = tweet.replace(link,"")
    return tweet

def take_tags(tweet):
    import re
    hash_tags=re.findall(r'#\w+', tweet)
    name_tags=re.findall(r'@\w+', tweet)
    return tweet,hash_tags,name_tags

'''cleans the tweets and adds the info in tree lists'''
def clean_tw(tweets):
    import re
    import urlmarker
    symbols="#,.\"\\:[]<>1234567890$%^&*;?/-_+=)("
    tw_l=[]
    ht_l=[]
    nt_l=[]
    for tweet in tweets:
        tw=tweet[1]
        tw=remove_links(tw)
        tw = tw.replace("@", " @")
        tw = tw.replace("#", " #")
        tw,ht,nt=take_tags(tw)
        tw=remove_chars(tw,symbols)
        tw_l.append( [tw,ht,nt ])
        ht_l+=ht
        nt_l+=nt
    return tw_l,ht_l,nt_l
