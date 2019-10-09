# while.py
''' Calculates the average of a list of grades'''

total = 0
counter = 0

grade = int(input('Enter grade, -1 to end: '))

while grade != -1:
    total += grade
    counter += 1
    grade = int(input('Enter gare, -1 to end: '))

if counter != 0:
    average = total /  counter
    print(f'The average is {average:.2f}')
else:
    print('No grades were entered')