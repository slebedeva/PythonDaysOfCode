# Write a program to print the first n numbers of a Fibonacci sequence
def print_fibonacci(n: int):
    """
    Prints first n numbers of Fibonacci sequence.
    Fibonacci sequence is where each number is the sum of 2 preceding ones.
    Special rule for start (when we have only 1).
    1
    sum(1) = 1
    sum(1,1) = 2
    sum(1,2) = 3
    sum(2,3) = 5
    sum(3,5) = 8
    etc.
    """
    if not isinstance(n, int):
        print('provide positive integer >= 1')
    else:
        print([fib(i) for i in range(1,n+1)])
    return None

def fib(n: int):
    # if invalid input
    if not isinstance(n, int) or n<=0:
        print('provide positive integer >= 1')
        return None
    # classbook recursive function - very bad for n=100!
    # special / conditions to stop
    #if n==1:
    #    return 1
    #elif n==2:
    #    return 1
    ## recursion: call itself
    #else:
    #    return fib(n-1) + fib(n-2) #sum of two preceding ones

    # closed form solution: O(n) to print n numbers
    # Binet's formula (see Wiki)
    golden_ratio = (5**0.5+1)/2
    return round((golden_ratio**n)/(5**0.5))

if __name__=="__main__":
    try:
        print_fibonacci(int(input('enter how many numbers from Fibonacci to print:')))
    except ValueError:
        print('provide integer >=1')
