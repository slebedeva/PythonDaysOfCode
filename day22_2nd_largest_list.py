# Create a program to find the second-largest element in a list.
def second_largest(inp: list):
    """ Returns second largest number in a list """
    if not isinstance(inp, list):
        raise TypeError('please provide a list')
    if not all([isinstance(element, (int,float)) for element in inp]):
        raise TypeError('please provide a list of numbers')
    if len(inp)<2:
        print('your list does not have 2 elements. returning None')
        return None
    return sorted(inp)[-2]

if __name__=="__main__":
    l = [9,3,5,7,4,2,-10,100.3]
    print(f'second largest in {l} is {second_largest(l)}')
