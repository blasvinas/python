# random_numbers.py

"""Call function that simulate a roll of a six-sided die"""

import random

def roll_dice():
    return random.randrange(1,7)

dice1 = roll_dice()
dice2 = roll_dice()

print(f'Dice1: { dice1}. Dice2: {dice2}.  Sum: {dice1 + dice2} ')
