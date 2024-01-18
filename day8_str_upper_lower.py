def str_upper_lower(inp: str):
    if not isinstance(inp, str):
        print('Please input a string')
        return None
    low = sum(s.islower() for s in inp)
    up = sum(s.isupper() for s in inp)
    return low, up

if __name__=="__main__":
    low, up = str_upper_lower(input('enter your string:'))
    print(f'your string has {low} lower and {up} upper characters')
