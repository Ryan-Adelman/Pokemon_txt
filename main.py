"""
what do I need to make pokemon 

trainer 
pokemon 
items

"""
import trainer.py
import pokemon.py
import items.py


def start():
    #first we need to get all the information to setup the main player and their rivala
    mp_gender = input("Welcome to the world of pokemon! Tell me, are you a Boy or a Girl?")
    while mp_gender.lower != 'boy' or mp_gender.lower != 'girl':
        mp_gender = input("Sorry what was that? Are you a Boy or a Girl")
    if(mp_gender.lower == 'boy'):
        mp_name = input("What is your name young lad?")
    elif(mp_gender.lower == 'girl'):
        mp_name = input("What is your name young lass?")
    else:
        mp_name = input("What is your name?")
    
    



