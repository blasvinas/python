# default_parameters.py
""" Shows how to use functions with keyword arguments """

def rectangle_area(length, width):
    return length * width

print(f'Area of a rectangle with length: 2 and width: 3 is {rectangle_area(width=3, length=2)}')
print(f'Area of a rectangle with length: 5 and width: 3 is {rectangle_area(length=5, width=3)}')
print(f'Area of a rectangle with length: 7 and width: 4 is {rectangle_area(7,4)}')