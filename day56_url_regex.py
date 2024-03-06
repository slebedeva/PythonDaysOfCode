# Create a function to extract all URLs from a given text using regular expressions

import re

# TODO: include queries after ? as well as pointers after #
pattern = "http[s]*://(?:[-\w]+\.)+[-\w]+(?:/[-\w]+)*"

text = input('Enter text:')

print('Your urls:')

print(re.findall(pattern, text))
