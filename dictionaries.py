# Create an English-French dictiorary

e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
print(f"Walrus in French is {e2f['walrus']}")

#  Create a French to English dictionary

f2e = {}
for english, french in e2f.items():
    f2e[french] = english
print(f2e)