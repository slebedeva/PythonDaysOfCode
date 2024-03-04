# Create a program that checks if a string is a palindrome
import string
def clean_string(s:str) -> str:
    """ Removes whitespaces, punctuationand turns to lower case"""
    return s.lower().translate(str.maketrans('', '', string.punctuation+' '))
    
def check_palindrome(inp:str) -> bool:
    """ Checks if a string is a palindrome (not counting whitespaces)"""
    s = clean_string(inp)
    return s == s[::-1]
