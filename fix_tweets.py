
def remove_chars(tweets,chars):
    for tweet in tweets:
        tweet[1] = ''.join( c for c in tweet[1] if  c not in chars )


#source:https://gist.github.com/gruber/8891611
def remove_links(tweets):
    import re
    import urlmarker
    for tweet in tweets:
        links=re.findall(urlmarker.URL_REGEX,tweet[1])
        for link in links:
            tweet[1] = tweet[1].replace(link,"")
