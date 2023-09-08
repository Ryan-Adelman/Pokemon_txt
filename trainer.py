from random import randint

"""
what does a trainer need?
-name
-gender
-pokemon 
-items
-money
-id
"""


class Trainer():
    def __init__(self, name, gender, pokemon, items, money):
        self.name = name
        self.gender = gender
        self.pokemon = pokemon
        self.items = items
        self.money = money
        self.id = randint(10**(10-1), (10**10)-1)
        print(self.id) 

