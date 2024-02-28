# Create a program that implements the bubble sort algorithm

# https://www.youtube.com/watch?v=Jdtq5uKz-w4

# Scan you array element by element
# If the next element is smaller, swap the two 
# The first pass is guaranteed to move the largest number
# to the end of the array
# Thus with each pass,
# the largest element in unsorted part will 
# move ('bubble up') to the end
# So we do not need to go through the sorted part 
# - improve efficiency a bit
# Worst time complexity is (n-1)*(n-1)*C = O(n**2)
# Another improvement:
# if the list is already sorted, no need to make more passes
# We can add 'flag' variable that is False until 1 swap occured
# Best-case O(n) 
# - if already sorted and all improvements implemented

def bubble_sort(A):
    """
    Implements the bubble sort algorithm.
    Input:
        A : the input array to be sorted
    A should be mutable.
    Output:
        sorted array.
    """
    n = len(A)
    next_run = True # to monitor if the list is sorted
    

    for i in range(n-1): #counter for runs (max n-1)
        if next_run:
            next_run = False # if no swap will happen in this run we stop
            for j in range(n-1-i): #counter for elements (less of them with each run)
                if A[j+1] < A[j]: # element swap condition
                    A[j], A[j+1] = A[j+1], A[j]
                    next_run = True #one more run needed if a swap happened
    
    return A

if __name__=="__main__":
    # generate a random list
    import random
    list = [random.randint(1,100) for _ in range(100)]
    print(list)
    print(f'sorted: {bubble_sort(list)}')
