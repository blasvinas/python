#Shows how to use lists and tuples
year_list = [1971, 1972, 1973, 1974, 1975]
print(f'My third bithday was on {year_list[3]}')
print(f'I was the oldest in {year_list[-1]}')

things = ["mozzarella","cinderella","salmonella"]
print(things[1].capitalize())
print(things)
things = [element.upper() for element in things]
print(things)
del things[2]
print(things)

surprise = ["Groucho","Chico","Harpo"]
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print(surprise)

even_numbers = [number for number in range(1,10) if number % 2 == 0]
print(even_numbers)
