# Write a program to find the most common words
# in a text file (how many?)

# General idea is to make a hash table

# sklearn has convenient libraries
from sklearn.feature_extraction.text import CountVectorizer

# others use Counter

def return_common_words(file_path, n=10):
    """
    Finds n most common words in a text file.
    Default 10.
    """
    with open(file_path,'r') as f:
        corpus = f.readlines()
    vectorizer = CountVectorizer()
    vectorizer.fit(corpus)
    # return n most common words:
    try:
        return sorted(vectorizer.vocabulary_.items(), key = lambda item:item[1])[-n:]
    except IndexError:
        print(f'Cannot return {n} words, you have less in your corpus.')
