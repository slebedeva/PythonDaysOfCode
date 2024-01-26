# Write a function that counts the frequency of each word in a sentence.
import re
from string import punctuation
from collections import Counter #more efficient than counting in a loop
def count_tokens(sentence: str):
    """Counts words in a sentence or several sentences.
        Does not use nltk or sklearn CountVectorizer."""
    #do not forget: lower(), remove punctuation, remove digits
    # TODO: more efficient with regex
    sentence = ''.join(char for char in sentence if not char.isdigit())
    # strip punctuation, put to lower, split into words avoiding empty string
    words = [w.strip(punctuation) for w in sentence.lower().split()]
    words = [w for w in words if w!='']
    # filter out empty strings
    # it is faster with the set
    return Counter(words)

if __name__=="__main__":
    sentence = input('your sentence, please:')
    print(count_tokens(sentence))
