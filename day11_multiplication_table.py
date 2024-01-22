# Write a program to print the multiplication table of a given number.
def mult_table(inp: int):
    if not isinstance(inp, int):
        print("Provide integer please")
        return None
    else:
        return {i:inp*i for i in range(1,inp+1)}

if __name__=="__main__":
    try:
        inp = int(input('your number:'))
        print(mult_table(inp))
    except ValueError:
        print('Please provide integer!')
