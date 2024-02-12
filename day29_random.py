# Create a function that generates a random number between a given range.

# random is completely deterministic
# in version 3.11: The seed must be one of the following types: None, int, float, str, bytes, or bytearray
# for cryptography, use secrets module
# return float because it does not care about the order :-)

import random

def give_random(start, end, seed=None):
    """
    Generate a random number between a given range.

    Parameters:
    - start (float): The lower bound of the range.
    - end (float): The upper bound of the range.
    - seed (None, int, float, str, bytes, or bytearray): The seed value for random number generation. If None, the random number generator is initialized based on the system time.

    Returns:
    - float: A random number between the given range.
    """
    random.seed(seed)
    return random.uniform(start, end)
    