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
    #what every trainer needs
    def __init__(self, name, gender, pokemon, items, money):
        self.name = name
        self.gender = gender
        self.pokemon = pokemon
        self.items = items
        self.money = money
        self.id = randint(10**(10-1), (10**10)-1)
        print(self.id) 
    #what happens when you try to print the whole trainer 
    def __repr__(self):
        return "{name} you have {money} money,/n{pokemon} pokemon,/nand {items} items}".format(name = self.name, money = self.money, pokemon = self.pokemon, items = self.items)
    #grabing the info we would want from the trainer
    def get_name(self):
        return self.name
    def get_pokemon(self):
        return self.pokemon
    def get_items(self):
        return self.items
    def get_money(self):
        return self.money
    def get_id(self):
        return self.id

    #ways to increse the money the trainer has

    def gain_money(self, amount):
        self.money += amount 
        print("{name} now have {money} money".format(name = self.name, money = self.money))
    def lose_money(self,amount):
        #if we have less money that what we are losing
        if(self.money < amount):
            print("{name} you do not have enough money")
        else:
            self.money -= amount 
        print("{name} you have {money} money now.")
    

    
