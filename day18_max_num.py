# Create a program to find the largest among three numbers.

if __name__=="__main__":
    try:
        num1 = float(input('first num:'))
        num2 = float(input('second num:'))
        num3 = float(input('third num:'))
        print(f'the largets number is {max([num1,num2,num3])}')
    except ValueError:
        print('please enter numbers')
