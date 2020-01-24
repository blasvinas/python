# Create a set with odd number using comprehensions
odd_numbers = { number for  number in range(0,10) if number % 2 != 0}
print(odd_numbers)

#Create a set with the even numbers using comprehension
even_numbers = { number for number in range(0, 11) if number % 2 == 0}
print(even_numbers)

#Get the union between odd_numbers and even_numbers
numbers = even_numbers | odd_numbers
print(numbers)