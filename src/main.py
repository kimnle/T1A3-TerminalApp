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
    if level.lower() == "e":
        max = 10
        attempts = 5
    elif level.lower() == "m":
        max = 100
        attempts = 10
    elif level.lower() == "h":
        max = 1000
        attempts = 15
    else:
        print("Can only type E, M or H")

def player_guess():
    number = random.randint(1, max)
    guess = int(input(f"Guess the number I am thinking of between 1 and {max}: "))