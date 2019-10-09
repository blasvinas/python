#Dictionary to hold person info
person = {'first_name':'Blas','last_name':'Vinas','age':46,'city':'Jacksonville'}

print("First Name: {}".format(person['first_name']))
print("Last Name: {}".format(person['last_name']))
print("Age: {}".format(person['age']))
print("City: {}".format(person['city']))

#Using a loop to print the dictionary
print("\nUsing a loop to print the dictionary")
for key, value in person.items():
    print("{} : {}".format(key,value))

print("\nPrinting the keys")
for key in person.keys():
    print(key)

print("\nPrinting the values")
for value in person.values():
    print(value)

#A list of dictionaries
person1 = {'first_name':'Blas','last_name':'Vinas','age':46,'city':'Jacksonville'}
person2 = {'first_name':'Yady','last_name':'Salas','age':43,'city':'Jacksonville'}
person3 = {'first_name':'Natalia','last_name':'Vinas','age':16,'city':'Jacksonville'}
person4 = {'first_name':'Andrea','last_name':'Vinas','age':13,'city':'Jacksonville'}
person5 = {'first_name':'Alejandro','last_name':'Vinas','age':11,'city':'Jacksonville'}

people = [person1, person2, person3, person4, person5]

for person in people:
    print('\n')
    for key, value in person.items():
        print("{}: {}".format(key,value))

#A list in a dictionary
person_languages = {'name':'Blas',"languages": ['Spanish', 'English']}
print("\n{} speaks the following languages:".format(person_languages['name']))
for language in person_languages['languages']:
    print(language)

