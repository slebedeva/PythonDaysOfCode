# Write a program that uses recursion to generate all permutations of a list

import itertools

def permute_list(l:list) -> list:
    # no recursion
    return list(itertools.permutations(l))
    
def permute_list_recursive(l:list) -> list:
    # if empty list or one element, return itself
    if len(l) < 2:
        return l
    # recursion part
    # put each element at the beginning of the list and add recursion calling on the remaining list
    else:
        ans = [] #container to append the answer to
        for i,el in enumerate(l):
            ans.extend([[el]+rest if isinstance(rest,list) else [el]+[rest] for rest in permute_list_recursive(l[:i]+l[i+1:])] )
        return ans
        
if __name__=="__main__":
    l = list(range(4))
    print(f'all permutations of {l} are {permute_list_recursive(l)}')
