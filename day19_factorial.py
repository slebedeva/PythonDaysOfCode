# Write a function to calculate the factorial of a number.
import math

# by hand
def factorial(n: int):
    i = 1
    for j in range(1, n+1):
        i = i*j
    return i


if __name__=="__main__":
    try:
        print(math.factorial(int(input('Enter number:'))))
    except ValueError:
        print('Enter positive integer')
