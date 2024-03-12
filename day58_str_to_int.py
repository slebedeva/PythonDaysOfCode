# Create a function that converts a string to an integer and handles ValueError

def str2int(s:str) -> int:
    """ Converts string to integer """
    try:
        return int(s)
    except ValueError as e:
        print(e)
        print('Provide an integer input')
        
    
if __name__=="__main__":
    print(str2int(input('your integer:')))
