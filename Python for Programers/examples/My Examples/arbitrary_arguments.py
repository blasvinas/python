# arbitraty_arguments.py
''' Shows how to use an arbitrary number of arguments '''

def average(*args):
    return sum(args)/len(args)

print(f'Average of 5,8,2,4,6,9 is  { average(5,8,2,4,6,9)}')