# Create a program that swaps the values of two variables.
def swap_variables(a,b):
    b,a = a,b
    return a,b

if __name__=="__main__":
    a = 4
    b = 'foo'
    print(f'a={a}, b={b}')
    a,b=swap_variables(a,b)
    print(f'a={a}, b={b}')
