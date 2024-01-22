# Write a program to reverse a given string.
def invert_str(inp: str):
    if not isinstance(inp,str):
        print('please provide string')
        return None
    else:
        return inp[::-1]

if __name__=="__main__":
    print(invert_str(input('enter string:')))
