import random

def game_title():
    print("Guess the Number Game")

def player_name():
    while True:
        try:
            name = input("Player name: ")
            if not name:
                raise ValueError("Cannot be empty")  
            else:
                print(f"Hey {name}")
                break
        except ValueError as e:
            print(e)
    

def game_play():
    level = input("Choose level - E for Easy, M for Medium or H or Hard: ")
    if level.lower() == "e":
        max = 10
        attempts = 5
    elif level.lower() == "m":
        max = 100
        attempts = 8
    elif level.lower() == "h":
        max = 1000
        attempts = 15
    else:
        print("Can only type E, M or H")
    number = random.randint(1, max)
    attempt = 0
    while attempt < attempts:
        guess = int(input(f"Guess the number that I am thinking of between 1 and {max}: "))
        if guess < number:
            print("Higher")
            attempt += 1
            attempts_left = attempts - attempt
            if attempts_left == 1:
                print(f"{attempts_left} attempt left")
            else:
                print(f"{attempts_left} attempts left")
        elif guess > number:
            print("Lower")
            attempt += 1
            attempts_left = attempts - attempt
            if attempts_left == 1:
                print(f"{attempts_left} attempt left")
            else:
                print(f"{attempts_left} attempts left")
        elif guess == number:
            print(f"Congrats!! You guessed it in {attempt} attempts")
            return
    else:
        print(f"You ran out of attempts, the number was {number}")

def play_again():
    again = input("Play again? Y or N: ")
    if again.lower() == "y":
        game_play()
        play_again()
    elif again.lower() == "n":
        print("Play again soon!!")
    else:
        print("Can only type Y or N")

if __name__ == "__main__":
    game_title()
    player_name()
    game_play()
    play_again()