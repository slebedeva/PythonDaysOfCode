# get synonyms with Ninja API - need to register for the key

import requests
import os

# get your key
ninja_key = os.getenv('ninja_api_key')

# collect user input
text = input('your text:')
word = input('word to replace:')

# construct url
api_url = 'https://api.api-ninjas.com/v1/thesaurus?word={}'.format(word)

# get the API repsonse
print('looking up the word in the dictionary...')
response = requests.get(api_url, headers={'X-Api-Key': ninja_key})
if response.status_code == requests.codes.ok:
    synonyms = response.json()['synonyms']
    # present them to the user
    for i,s in enumerate(synonyms):
        print(f'{i+1}:{s}')
else:
    print("Error:", response.status_code, response.text)

# let the user select what they want to use
try:
    index = int(input('Select the synonym to use:'))-1
except ValueError as v:
    print(v)
    print('please enter a valid index of the synonym')

# replace the word
print(text.replace(word, synonyms[index]))
