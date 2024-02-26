# Write a program that reads an integer from the user and handles invalid inputs

def read_integer_input():
    try:
        return int(input('enter your number:'))
    except ValueError as ve:
        print(ve)
        print('please enter an integer')

if __name__=="__main__":
    read_integer_input()
