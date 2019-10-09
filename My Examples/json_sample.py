import json

numbers = [10,5,8,9,3]

with open("numbers.json","w") as f:
    json.dump(numbers,f)

with open("numbers.json") as f:
    my_numbers = json.load(f)

print(my_numbers)