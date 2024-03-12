# Create a function that checks if a number is a perfect square

def is_perfect_square(n) -> bool:
    """Checks if a number is a perfect square"""
    try:
        return n**0.5==int(n**0.5) #.is_integer() #int(math.pow(number, .5)) == int(number)
    except ValueError as e:
        print(e)
        print('please provide a number')
