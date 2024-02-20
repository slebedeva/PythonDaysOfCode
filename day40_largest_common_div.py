# Write a function to find the largest common divisor of two numbers using a function

def lcd_naive(a, b):
    """ Find largest common divisor of two numbers.
        Using Euclidian method (see Wikipedia)
        Replace one of the two numbers 
        by the modulo of division of one to the other.
        As soon as one of them is 0, return the other."""
    while b>0:
        a,b = b, a%b
    return a

from math import gcd
def lcd_quick(a, b):
    return gcd(a, b)
