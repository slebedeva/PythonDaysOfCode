# Create a program that sorts a list of strings alphabetically.

# I stop checking for input inside function now

#sorted() can take key = custom_function or lambda, for example key=len will sort from short to long
def sort_strings_list(inp: list[str]) -> list[str]:
    return sorted(inp) 
