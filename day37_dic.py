# Write a program to iterate through a dictionary and print its keys and values
def print_dic(inp:dict):
    try:
        for k,v in inp.items():
            print(f'{k}:{v}')
    except AttributeError:
        print('please provide a dictionary')
