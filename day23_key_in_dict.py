# Write a program that checks if a key exists in a dictionary.

def key_in_dict(inp:dict,k):
    if not isinstance(inp, dict):
        raise TypeError('please provide a dictionary')
    return k in inp
