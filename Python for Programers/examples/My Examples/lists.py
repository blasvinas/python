# my_list.py
''' Shows how to use lists '''

def print_list(my_list):
    for i, item in enumerate(my_list):
        print(f'{i}: {my_list[i]}, ',end=' ')
    print()

my_list = [item for item in range(1,11)] # Generates a list with elements from 1 to 10  using list comprehension
print_list(my_list)

# print every other element
for item in my_list[::2]:
    print (f'{item}, ', end=' ')
print()

# print elements in reverse order
for item in my_list[len(my_list) - 1::-1]:
    print(f'{item}, ',end=' ')
print()

#Add elements to the list
my_list.append(11)
print_list(my_list)

#Remove element from ther list
del my_list[10]
print_list(my_list)

#Sorting the list in reverse order
my_list.sort(reverse=True)
print_list(my_list)

#Sorting the list
my_list.sort()

#Searching for an element
if 5 in my_list:
    print(f'5 is in index {my_list.index(5)}')

#print even numbers using list comprehension
even_numbers = [item for item in my_list if item %2 == 0]
print_list(even_numbers)

#printing odd number using filter
def is_odd(x):
    return x % 2 != 0

odd_numbers = list(filter(is_odd, my_list))
print_list(odd_numbers)

#printing odd number using filter and lambda
odd_numbers = list(filter(lambda x: x%2 != 0, my_list))
print_list(odd_numbers)

#mapping values to new values
squares = list(map(lambda x: x ** 2, my_list))
print_list(squares)