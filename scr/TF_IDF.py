from sklearn.feature_extraction.text import TfidfVectorizer

def TF_IDF():
    vectorizer = TfidfVectorizer(stop_words="english", strip_accents="ascii", lowercase=True)
    #TODO use rafa's tokenization instead of file?
    file = open("/home/nem/PycharmProjects/SentimentAnalysis/twitter_data/test.tsv")
    tfidf_matrix = vectorizer.fit_transform(file)
    file.close()

    return tfidf_matrix #.toarray()
