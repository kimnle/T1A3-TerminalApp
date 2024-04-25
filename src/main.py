import random

def game_title():
    print("Guess the number!!")

def player_name():
    try:
        name = input("Player name: ")
        if not name:
            raise ValueError("Cannot be empty")
        else:
            print(f"Hey {name}")
    except ValueError as e:
            print(e)

def game_level():
    level = input("Choose level - E for Easy, M for Medium or H or Hard: ")