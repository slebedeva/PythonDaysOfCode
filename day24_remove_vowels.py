# Write a program to remove vowels from a given string.

import re
vowels = 'aouie'

def remove_vowels(inp: str):
    if not isinstance(inp,str):
        raise TypeError('please provide a string')
    return re.sub('|'.join(vowels+vowels.upper()), '', inp) #actually use '[aeiouAEIOU]' 


if __name__=="__main__":
    print(f'result: {remove_vowels(input("your string:"))}')
