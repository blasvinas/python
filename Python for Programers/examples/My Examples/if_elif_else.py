#if_elif_else.py
'''Displays
 "A" for grades greater than or equal to 90,
"B" for grades in the range 80-89,
"C" for grades 70-79,
"D" for grades 60-69,
"F" for all other grades'''

grade = 92
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')
