import nltk
from nltk.corpus import wordnet

def replace(word, text):
    """Replaces given word with synonym in given text.
    Lets the user choose the synonym to use.
    If word is not in text, return text with no error."""


    # get a list of synonyms #  #https://towardsdatascience.com/synonyms-and-antonyms-in-python-a865a5e14ce8
    synonyms = []
    for syn in wordnet.synsets(word):
        for lm in syn.lemmas():
                synonyms.append(lm.name())#adding into synonyms

    synonyms = list(set(synonyms))
    
    # present them to the user
    for i,s in enumerate(synonyms):
        print(f'{i+1}:{s}')

    try:
    # let the user select what they want to use
        index = int(input('Select the synonym to use:'))-1
    except ValueError as v:
        print(v)
        print('please enter index of the synonym')

    return text.replace(word,synonyms[index])

text = input('your text:')
word = input('word to replace:')
print(replace(word,text))
