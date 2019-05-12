import gensim as gensim


def Word2Vec(tweet_list=None, filename=None):
    tokenized_tweets = []   #list of tokenized tweets

    if tweet_list is not None:
        tokenized_tweets = [tweet.split() for tweet in tweet_list]
        print(tweet_list)
    elif filename is not None:
        with open(filename) as f:
            for line in f.readlines():
                tokenized_tweets.append(line.split())
                print(line, tokenized_tweets)

    model_w2v = gensim.models.Word2Vec(tokenized_tweets, size=50, window=5, min_count=2, sg=1)
    model_w2v.train(tokenized_tweets, total_examples=len(tokenized_tweets), epochs=20)
    return model_w2v

def WordEmbeddingsVectorize(tweet_list):
    model = Word2Vec(tweet_list=tweet_list)
    #calculate mean vector for every tweet
    for tweet in tweet_list:


    #save model to memory using pickle

print(list(Word2Vec(filename="/home/nem/PycharmProjects/SentimentAnalysis/resources/twitter_data_small.tsv")["Obama"]))