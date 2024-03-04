
def find_vowel_words(sentence:str) -> set:
    """ Finds all words that start with a vowel """
    vowels = 'aouie'
    return set([word for word in sentence.lower().split(' ') if word.lower()[0] in vowels])
