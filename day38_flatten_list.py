# Write a program to flatten a nested list
import itertools

def flatten_list(l:list) -> list:
    """
    Flatten a nested list using recursion.
    """  
    ans = []
    for e in l:
        if isinstance(e,list):
            ans.extend(flatten_list(e))
        else:
            ans.append(e)
    return ans           
