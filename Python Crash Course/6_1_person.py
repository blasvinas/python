person = {
    'first_name': 'Blas',
    'last_name': 'Vinas',
    'age': 47,
    'city': 'Jacksonville',
    }

print(person)

for key, value in person.items():
    print(key + " : " + str(value) )

print("Keys:")
for key in person.keys():
    print(key)

print("Values:")
for value in person.values():
    print(value)