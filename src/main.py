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

def validate_guess(guess, number, attempts):
    attempts_counter = 0
    while attempts_counter < attempts:
        if guess < number:
            print("Higher")
            attempts_counter += 1
        elif guess > number:
            print("Lower")
            attempts_counter += 1
        elif guess == number:
            print(f"You guessed it in {attempts_counter} attempts!")
            return
    else:
        print(f"You ran out of attempts, the number was {number}")

def play_game():
    again = "y"
    while again.lower() == "y":
        again = input("Play again? Y or N: ")
    print("Play again soon!!")