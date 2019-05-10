
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

def remove_tags(tweet):
    tweet = " ".join(filter(lambda x:x[0]!='@', tweet.split()))
    tweet = " ".join(filter(lambda x:x[0]!='#', tweet.split()))
    return tweet


def wd_rem(tweets):
    import re
    import urlmarker
    symbols="#@,.'\"\\:[]<>1234567890!$%^&*;?/-_+=)("
    tw_l=[]
    for tweet in tweets:
        tw=tweet[1]
        tw=remove_links(tw)
        tw = tw.replace("@", " @")
        tw = tw.replace("#", " #")
        tw=remove_tags(tw)
        tw=remove_chars(tw,symbols)
        tw_l.append(tw)
    return tw_l
