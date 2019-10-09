import functions as f
f.make_shirt("Hello World","small")
f.make_shirt(size="medium", message="I love Python")
f.make_shirt("I love C++ better")

print(f.city_country("Barranquilla","Colombia"))
print(f.city_country("Jacksonville"))

magicians = ['Pepe','Tono','Lola']
great_magicians =  f.make_great_magicians(magicians)
print(magicians)
print(great_magicians)


f.make_pizza("cheese")
f.make_pizza("pineapple","ham")
f.make_pizza("peperonni","ham","sausage")


user_profile = f.create_user_profile("Blas","Vinas",age=47,ocupation='IT Manager')

print(user_profile)
