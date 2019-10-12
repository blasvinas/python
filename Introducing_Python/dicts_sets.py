#Shows how toi work with dictionaries

e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f["walrus"])
f2e = {}
for en, fr in e2f.items():
    f2e[fr] = en
print(f2e["chien"])

life = {"animals": {"cats": ["Henri","Grumpy","Lucy"],"octopi": {},"emus": {}},"plants": {},"other": {}}
print(life.keys())
print(life["animals"].keys())
print(life["animals"]["cats"])

squares = {number: number ** 2 for number in range(1,10) }
print(squares)

odd = {number for number in  range(10) if number % 2 != 0}
print(odd)

numbers = (f"Got {number}" for number in range(10))
for number in numbers:
    print(number)

keys = ("optimist","pessimist","troll")
values = ("The glass is half full","The glass is half empty","How did you get a glass?")

my_dict = {}
for key, value in zip(keys, values):
    my_dict[key] = value
print(my_dict)

titles = ["Creature of Habit","Crewel Fate","Sharks On a Plane"]
plots = ["A nun turns into a monster","A haunted yarn shop","Check yoiur exists"]
movies = {}
for title, plot in zip(titles, plots):
    movies[title] = plot
print(movies)