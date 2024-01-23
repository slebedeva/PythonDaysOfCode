# Write a program to shuffle the elements of a list randomly.
"""
This program will shuffle your input list randomly.
You can provide seed in commandline.
Default seed is 42.
"""
import random

# add seed as commandline argument
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--seed", help="enter integer seed for random shuffling", type = int, default = 42)
# verbosity is boolean
parser.add_argument("-v", "--verbose", help="increase output verbosity"
                    #,type = int, choices = [0,1]
                    , action="store_true")
args = parser.parse_args()
# seed is optional
if args.verbose:
    if args.seed:
        print(f'your seed is {args.seed}')
def shuffle_list(inp: list, seed : int=42):
    if not isinstance(inp, list):
        inp = list(inp)
    random.seed(seed)
    random.shuffle(inp)
    return inp

if __name__=="__main__":
    l = list(range(10))
    print(f'{l} shuffled : {shuffle_list(l, args.seed)}')
