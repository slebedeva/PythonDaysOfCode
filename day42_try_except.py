# Write a program that uses a try-except block to handle division by zero

def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('cannot divide by zero')
    except TypeError:
        print('please enter numbers')

if __name__=="__main__":
    try:
        divide(float(input('first number:')),
           float(input('second number:')))
    except ValueError:
        print('please enter numbers')
