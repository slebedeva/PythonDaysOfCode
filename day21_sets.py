# Create a program to remove a specific element from a set.

def remove_from_set(inp:set, element)-> set:
    """Removes element from set"""
    # if input is not a set, convert to it, no error
    # string will be split up into chars
    if not isinstance(inp,set):
        print('Converting to set...')
        inp = set(inp)
    # update input
    inp.discard(element) #better use inp.discard() than inp.remove() as it does not raise en error
    return inp

if __name__=="__main__":
    s = set(range(10))
    e = 8
    print(f'removing {e} from {s} results in {remove_from_set(s,e)}')
