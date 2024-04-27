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
        except ValueError as a:
            print(a)
    
def game_play():
    while True:
        try:
            level = input("Choose level - E for Easy, M for Medium or H or Hard: ")
            if level.lower() == "e":
                max = 10
                attempts = 5
                break
            elif level.lower() == "m":
                max = 100
                attempts = 8
                break
            elif level.lower() == "h":
                max = 1000
                attempts = 15
                break
            else:
                raise ValueError("Please type E, M or H only")
        except ValueError as b:
            print(b)

    number = random.randint(1, max)
    attempt = 0

    while attempt < attempts:
        while True:
            try:
                guess = int(input(f"Guess the number that I am thinking of between 1 and {max}: "))
                if 1 <= guess <= max:
                    break
                else:
                    print(f"Please enter a number between 1 and {max} inclusive")
            except ValueError:
                    print("Please enter numbers only")

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
    while True:
        try:
            again = input("Play again? Y or N: ")
            if again.lower() == "y":
                game_play()
                play_again()
                break
            elif again.lower() == "n":
                print("Play again soon!!")
                break
            else:
                raise ValueError("Please type Y or N only")
        except ValueError as c:
            print(c)

if __name__ == "__main__":
    game_title()
    player_name()
    game_play()
    play_again()