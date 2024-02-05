# Create a program to concatenate two lists.

def concat_2_lists(l1:list, l2:list):
    if not (isinstance(l1, list) and isinstance(l2, list)):
        raise TypeError('both inputs must be lists')
    l1.extend(l2)
    return l1 #or l1+l2 #or itertools.chain()
