# Write a program to find the maximum and minimum values in a list.
def get_minmax(inp: list):
    return min(inp), max(inp)

if __name__=="__main__":
    l = [1,2,3]
    print(f'min, max of {l} = {get_minmax(l)}')
