# Write a program that removes all whitespaces from a given string

import sys

# TODO: take the string as commandline argument

def remove_whitespace(inp:str)->str:
    return inp.replace(' ','')

if __name__=="__main__":
    print(f'your answer: {remove_whitespace(input("your string:"))}')

