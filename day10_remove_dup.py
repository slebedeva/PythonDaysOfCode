# Write a program to remove duplicates from a list.
def remove_duplicates(inp: list):
    if not isinstance(inp, list):
        print('please provide a list')
        return None
    else:
        ans = []
        for i in inp:
            if not i in ans:
                ans.append(i)
        return ans

if __name__=="__main__":
    inp = [3,4,'foo',4,5,'bar','bar']
    print(f'For {inp} the unique list is {remove_duplicates(inp)}')
