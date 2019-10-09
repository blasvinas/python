pizzas = ["peperoni","supreme","pinneaple and ham","BBQ Chicken","Meat Lovers","Cheese"]

for pizza in pizzas:
    print("I like " + pizza.title() + " pizza")

print("I will order pizza this weekend")

#Counting to 10
print("Number from 1 to 10:")
for number in range(1,11):
    print(number)

#print odd number
print("odd numbers between 1 and 10")
for number in range(1,11,2):
    print(number)

#Numbers between 1 and 10 raised to the 3er power
for number in range(1,11):
    print(str(number) + " raised to the 3er power is " + str(number**3))

#Slices

my_pizzas = pizzas[:]  #Copy list pizzas to my_pizzas
print("The complete pizzas list:")
(print(my_pizzas))

print("First 3 items of pizzas are: ")
print(my_pizzas[:3])

print("The middle items in the list are:")
print(my_pizzas[2:5])

print("The last 3 items in the list are:")
print(my_pizzas[-3:])

