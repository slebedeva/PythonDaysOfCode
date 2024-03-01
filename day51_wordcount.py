# Create a program that counts the occurrences of each word in a text file
# some use https://github.com/sloria/textblob

from collections import Counter
import sys

def count_words(file_path: str) -> Counter:
    with open('text', 'r') as f:
        text = f.readlines()
    return Counter(' '.join(text).strip().lower().split(' '))

def main():
    """ Count words in a text."""    
    try:
        path = sys.argv[1]
        print(count_words(path))
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <path_to_file>")

if __name__=="__main__":
    main()
