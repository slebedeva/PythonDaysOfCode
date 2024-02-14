# Write a Python program to merge two dictionaries

# https://stackoverflow.com/a/26853961
# Python 3.9 z = x | y
# Python 3.5 z = {**x, **y}
# the second dictionary always overwrites the first if there are duplicate keys
 
# Python2 compatible:
def merge_dict(d1:dict, d2:dict):
    d = d1.copy()
    d.update(d2)
    return d
