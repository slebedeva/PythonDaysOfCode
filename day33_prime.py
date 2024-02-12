# Write a test case for a function that checks if a number is prime

# slow algorithm: check if dividable for every n between 2 and sqrt(n)

def is_prime(number:int) -> bool:
    """
    Checks if a number is prime with slow algorithm.
    """
    return not any([number%n==0 for n in range(2,int(number**0.5))])
