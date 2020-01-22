#Create a list with numbers in words
my_list = ['one','two','three','four']

#Create a new list using list comprehension with item capitalized
new_list = [number.capitalize() for number in my_list]
print(new_list)

#Create a new list sprted alphabetically
new_list = sorted(my_list)
print(new_list)

#add a element to the list
my_list.append('five')
print(my_list)

#Delete the first item
del my_list[0]
print(my_list)
