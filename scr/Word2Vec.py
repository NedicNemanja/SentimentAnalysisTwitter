

def Word2Vec(tokenized_tweets):
    model_w2v = gensim.models.Word2Vec(tokenized_tweets, size=50, windows=5, )