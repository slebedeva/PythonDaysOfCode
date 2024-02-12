# Create a function that finds the second smallest element in a list.

def second_smallest(inp:list):
    """
    Return second smallest element in a list
    Of course the list should be numeric, not mixed.
    """
    if not all([isinstance(el,(int,float)) for el in inp]):
        raise TypeError('please provide a list of numbers')
    return sorted(inp)[1]
