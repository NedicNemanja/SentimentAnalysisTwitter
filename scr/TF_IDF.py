from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english", strip_accents="ascii", lowercase=True)

file = open("/home/nem/PycharmProjects/SentimentAnalysis/twitter_data/test.tsv")
tfidf_matrix = vectorizer.fit_transform(file)
file.close()

print(tfidf_matrix.toarray()[1])

