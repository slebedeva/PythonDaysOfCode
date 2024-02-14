# Write a simple unit test for a function that adds two numbers


def add_two(x,y):
    if not all([isinstance(num,(int,float)) for num in (x,y)]):
        raise TypeError('please provide numbers')
    return x+y
