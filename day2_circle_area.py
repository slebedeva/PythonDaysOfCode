# Create a program to calculate the area of a circle given its radius.
import math
def get_area(radius):
    # exceptions / constraints
    if (not type(radius) in [int,float]) or (isinstance(radius, bool)):
        print("Your radius whould be a real positive number")
        return None #this will allow code to continue
    if radius < 0:
        print("Your radius should be positive")
        return None
    try:
        area = math.pi*(radius**2)
    except OverflowError: #handle floating point limit
        print("Radius too large, returning inf")
        return math.inf
    return area

if __name__=="__main__":
    radius = float(input("Enter radius:"))
    print(f'Answer: {get_area(radius)}')
