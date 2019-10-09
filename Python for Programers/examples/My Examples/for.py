# for.py
''' Calculates the average of a list of grades'''

total = 0
counter = 0

grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]

for grade in grades:
    total += grade
    counter += 1

average = total /  counter
print(f'The average is {average}')