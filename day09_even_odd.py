# Write a program to check if a number is even or odd.
def even_odd(inp:int):
    if not isinstance(inp, int):
        print('please provide an integer')
        return None
    else:
        return 'odd' if inp%2==1 else 'even'

if __name__=="__main__":
    try:
        print(even_odd(int(input('your number:'))))
    except ValueError:
        print('please enter an integer')
