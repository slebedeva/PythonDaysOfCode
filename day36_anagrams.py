# Write a Python program to check if two strings are anagrams
# Anagrams are words made up of the same letters like New York Times = monkeys write
# Whitespaces do not count (otherwise celver people just use sorted(s1)==sorted(s2) and compare)
# My naive approach: make a dictionary of each, excluding spaces, check if dicts are identical
# Anagram solvers use an anatree / hash table structures to search anagrams in constant time

# more efficient than dict comprehension
from collections import Counter

def make_dic(s):
        return Counter(s.lower().replace(' ', ''))
    
def are_anagrams(s1:str, s2:str): 
    """
    Given two strings, returns true if they are anagrams.
    Whitespaces do not count.
    Will try to convert non-string input to string.
    """
    try:
        s1 = str(s1)
        s2 = str(s2)
    except TypeError:
        raise TypeError('both inputs must be strings')
    return make_dic(s1)==make_dic(s2)

if __name__=="__main__":
    s1 = input('input first string:')
    s2 = input('input second string:')
    if are_anagrams(s1,s2):
        print(f'{s1} and {s2} are anagrams')
    else:
        print(f'{s1} and {s2} are not anagrams')
