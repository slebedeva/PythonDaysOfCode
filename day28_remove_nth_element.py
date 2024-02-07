# Create a program that removes the nth element from a list.

# altenrtaives: 
# del inp[n] #it modifies the input - not good unless explicitly wanted!
# list.remove(list[n])
# list.pop(n-1)
# slicing(pythonic! l[:n]+l[n+1:]) - but not for negative n
# filter() (functional) - written in C so faster 
# returns iterator object - more memory efficient than for loop
# https://realpython.com/python-filter-function/#coding-with-functional-style-in-python
# if you pass None it will use identity funciton and return truthy objects

def remove_element(inp: list, n:int):
    """
    Removes element from a list assuming 0-based indexing
    Error if the list is shorter than n-1
    If n<0 it will count from the end"""
    if not (isinstance(inp,list) and isinstance(n, int)):
        raise TypeError('input must be a list and index am integer')
    if len(inp)<=abs(n):
        raise IndexError('the list is shorter than n')
    return list(filter(lambda el:el!=inp[n], inp))
