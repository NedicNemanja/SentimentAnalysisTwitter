import gensim as gensim
from nltk.tokenize import TweetTokenizer
import pickle


def Word2Vec(tweet_list):

    tokenized_tweets = [tweet[0] for tweet in tweet_list]

    model_w2v = gensim.models.Word2Vec(tokenized_tweets, size=50, window=5, min_count=2, sg=1)
    model_w2v.train(tokenized_tweets, total_examples=len(tokenized_tweets), epochs=20)
    return model_w2v


def WordEmbeddingsVectorize(tweet_list, size=200, pkl_filename=None):
    model = Word2Vec(tweet_list)
    tz = TweetTokenizer(strip_handles=True, reduce_len=True)
    # calculate mean vector for every tweet
    tweet_vectors = []
    for tweet in tweet_list:
        tweet_vector = [0]*size
        for token in tz.tokenize(tweet[0]):
            try:
                tweet_vector = [x+y for x,y in zip(tweet_vector,model[token])]
            except KeyError:
                pass
        tweet_vector = [x/size for x in tweet_vector]
        tweet_vectors.append(tweet_vector)
    print(tweet_vectors)
    if pkl_filename is not None:    #save vectorized tweets to disk
        with open(pkl_filename,"w+") as file:
            pickle.dump(tweet_vectors, file, protocol=pickle.HIGHEST_PROTOCOL)
    return tweet_vectors
