# Write a function to count the number of vowels in a given string
import re

def count_vowels(inp: str):
    if not isinstance(inp, str):
        raise TypeError('input should be text')
    if len(inp)==0:
        return 0
    vowels = 'aouie'
    return sum([inp.lower().count(vowel) for vowel in vowels])

if __name__=="__main__":
    print(count_vowels(input("input your string:")))
