person1 = {
    'first_name': 'Blas',
    'last_name': 'Vinas',
    'age': 47,
    'city': 'Jacksonville',
    'food': ['steak', 'sushi', 'soup'],
    }

person2 = {
    'first_name': 'Yady',
    'last_name': 'Salas',
    'age': 44,
    'city': 'Jacksonville',
    'food': ['chicken','tomato soup', 'bread'],
    }

person3 = {
    'first_name': 'Natalia',
    'last_name': 'Vinas',
    'age': 17,
    'city': 'Jacksonville',
    'food': ['pasta', 'rice','arepa'],
    }

people = [person1, person2, person3]

for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))
    print()