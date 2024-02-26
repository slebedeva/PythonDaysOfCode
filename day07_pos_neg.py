def determine_sign(num):
    if not isinstance(num, (int, float)):
    #    raise TypeError('Input must be a number')
        print('Input error: please provide a number!')
        ans = None
    else: #important, otherwise it will still run through!
        ans = get_sign_value(num)
    return ans

def get_sign_value(num):
    if num == 0:
        return 'zero'
    elif num > 0:
        return 'positive'
    else:
        return 'negative'

if __name__=="__main__":
    try:
        print(determine_sign(float(input('Your number:'))))
    except ValueError:
        print('Provide a number')
