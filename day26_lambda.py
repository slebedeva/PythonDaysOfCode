# Create a program that uses a lambda function to square each element of a list.

def squared(inp: list):
    if not isinstance(inp, list):
        raise TypeError('Input must be a list')
    if not all(isinstance(el, (int,float)) for el in inp):
        raise TypeError('list elements must be real numbers')
    return [el**2 for el in inp] #we do not need lambda here or? OK, like this: list(map(lambda x : x**2, nums))
