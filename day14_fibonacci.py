# Write a program to print the first n numbers of a Fibonacci sequence
import ipdb
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
        # TODO optimize this to return to memo too
        print([fib(i,{}) for i in range(1,n+1)])
    return None

def fib(n: int, memo: dict[int, int]):
    # if invalid input
    if not isinstance(n, int) or n<=0:
        print('provide positive integer >= 1')
        return None

    # we can keep recursion but need to use dynamic programming
    # to avoid recalculating Fibonacci for the same number many many times
    # this is called memoization (sic) - store already calculated values
    # memo, dict to store values, needs to be argument of the recursive function
    if n in memo:
        return memo[n]
    if n in [1,2]:
        return 1
    # do not forget to record this into dict
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

    # closed form solution: O(n) to print n numbers
    # Binet's formula (see Wiki)
    #golden_ratio = (5**0.5+1)/2
    #return round((golden_ratio**n)/(5**0.5))

if __name__=="__main__":
    try:
        memo = {}
        print_fibonacci(int(input('enter how many numbers from Fibonacci to print:')))
    except ValueError:
        print('provide integer >=1')
