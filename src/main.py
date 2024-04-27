import random

def game_title():
    print("Guess the number!!")

def player_name():
    name = input("Player name: ")
    print(f"Hey {name}")

def level_guess():
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
    number = random.randint(1, max)
    attempts_counter = 0
    while attempts_counter < attempts:
        guess = int(input(f"Guess the number that I am thinking of between 1 and {max}: "))
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

def play_again():
    again = input("Play again? Y or N: ")
    if again.lower() == "y":
        level_guess()
    elif again.lower() == "n":
        print("Play again soon!!")

if __name__ == "__main__":
    game_title()
    player_name()
    level_guess()
    play_again()