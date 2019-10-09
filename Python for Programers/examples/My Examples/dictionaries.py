# dictionaries.py
''' Shows how to use dictionaries '''

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}

for month_number, month_name in months.items():
    print(f'{month_number} : {month_name}')

for key in months.keys():
    print(f'{key} : {months[key]}')
