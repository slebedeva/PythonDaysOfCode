# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

def return_even(inp: list[int]) -> list[int]:
    if not isinstance(inp,list):
        print('Input a list of integers')
        return []
    else:
        try:
            return [n for n in inp if n%2==0]
        except TypeError:
            print('Input a list of integers')
            return []

if __name__=="__main__":
    l = list(range(10))
    print(f'input: {l}, output {return_even(l)}')
