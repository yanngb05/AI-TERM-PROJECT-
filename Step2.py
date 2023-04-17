from sklearn.feature_extraction.text import CountVectorizer

corpus = [cleaned_tweet1, cleaned_tweet2]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(X.toarray())
