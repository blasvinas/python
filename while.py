# prints the even numbers
n = 0
while n <= 10:
    n += 1
    if n % 2 != 0:
        continue
    print(n)

# prints the numbers in the list until the  first negative  is found.
# If no negatives numbers are found a message is printed.
numbers = [1, 4, 8, 9]
n = 1
count = len(numbers)
while n < count:
    if numbers[n] < 0:
            break
    print(n)
    n += 1
else:
    print('No negatives numbers were found')
