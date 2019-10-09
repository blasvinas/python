import numpy as np

def display_array(array):
    for row in array:
        for column in row:
            print(column, end=' ')
        print()

def display_stats(array):
    print(f'Sum: {array.sum()}')
    print(f'Min: {array.min()}')
    print(f'Max: {array.max()}')
    print(f'Mean: {array.mean()}')

grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])
display_array(grades)
display_stats(grades)
