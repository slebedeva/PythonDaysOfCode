# Write a program to find the sum of all elements in a list.
def sum_list(inp: list):
    if not isinstance(inp, list):
        raise TypeError('Input must be a list')
    try:
        return sum(inp)
    except TypeError:
        raise TypeError('please enter numbers')


if __name__=="__main__":
    try:
        l = []
        for _ in range(int(input('Enter length of your list:'))):
            l.append(float(input('Enter numbers in your list: ')))
        print(f'Sum of the list{l} is {sum_list(l)}')
    except ValueError:
        print('Please enter numbers only')
