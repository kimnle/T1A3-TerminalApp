import random

def game_title():
    print("Guess the number!!")

def player_name():
    try:
        player_name = input("Player name: ")
        if not player_name:
            raise ValueError("Cannot be empty")
        else:
            print(f"Hey {player_name}")
    except ValueError as e:
            print(e)