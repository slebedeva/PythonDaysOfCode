# Create a function that takes a string and returns the reverse of each word

# some people use TextBlob (based on nltk and pattern)

def reverse_words(text:str) -> str:
    """Reverses every word in text"""
    # TODO: make sure punctuation is staying where it should
    return ' '.join([word[::-1] for word in text.split(' ')])
