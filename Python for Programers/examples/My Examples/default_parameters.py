# default_parameters.py
""" Shows how to use functions with default parameter values """

def rectangle_area(length=2, width=3):
    return length * width

print(f'Area of a rectangle with length: 2 and width: 3 is {rectangle_area()}')
print(f'Area of a rectangle with length: 5 and width: 3 is {rectangle_area(5)}')
print(f'Area of a rectangle with length: 7 and width: 4 is {rectangle_area(7,4)}')
