bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
print("First element: {}".format(bicycles[0]))

#last element
print("Print the last element: {}".format(bicycles[-1]))

#Add an element to the list
bicycles.append('honda')
print("List after adding an element: {}".format(bicycles))

#Insert and element at the second position
bicycles.insert(1,'yamaha')
print("List after inserting an element in the second position: {}".format(bicycles))

#Removing an element
del bicycles[1]
print("List after removing an element in the second position: {}".format(bicycles))

#Removing using pop
element = bicycles.pop()  #Remove the last element
print("List after removing the last element: {}".format(bicycles))
print('Element removed: {}'.format(element))
element = bicycles.pop(2)  #Remove 3er element
print("List after removing the 3er element: {}".format(bicycles))
print('Element removed: {}'.format(element))

#Removing by value
bicycles.remove('cannondale')
print("List after removing  'cannondale': {}".format(bicycles))

bicycles = ['trek','cannondale','redline','specialized']

#Sort the list (permanent)
bicycles.sort()
print("List after sorting: {}".format(bicycles))

#Sort in reverse (permanent)
bicycles.sort(reverse=True)
print("List after sorting in reverse: {}".format(bicycles))

#Temporary sort
print(sorted(bicycles))
print("List after sorted: {}".format(bicycles))

#Reverse the order or the list (not alphabetically)
bicycles.reverse()
print("List in reverse order: {}".format(bicycles))

#Length of the list
print("The length of the list is: {}".format(len(bicycles)))

#Looping the list
for byke in bicycles:
    print(byke)