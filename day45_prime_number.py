# Write a function to check if a number is a prime number

# we already did it by hand in day33 so let us use a library this time

import sympy # nice symbolic math library

def isprime(num:int) -> bool:
    return sympy.isprime(num)
