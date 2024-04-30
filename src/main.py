import random, os, csv

import pandas as pd

def game_title():
    print("Guess the Number Game")

def create_file(file_name):
    try:
        with open(file_name, "w") as f:
            f.write("Level,Player name,Attempts\n")
    except IOError:
        print("Could not create file")

def player_name():
    global name
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
            level = input("Choose level - easy, medium or hard: ")
            if level.lower() == "easy":
                max = 10
                attempts = 5
                break
            elif level.lower() == "medium":
                max = 100
                attempts = 8
                break
            elif level.lower() == "hard":
                max = 1000
                attempts = 10
                break
            else:
                raise ValueError("Please type easy, medium or hard only")
        except ValueError as b:
            print(b)

    number = random.randint(1, max)
    attempt = 1

    while attempt <= attempts:
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
            attempts_left = attempts - attempt + 1
            if attempts_left == 1:
                print(f"{attempts_left} attempt left")
            else:
                print(f"{attempts_left} attempts left")
        elif guess > number:
            print("Lower")
            attempt += 1
            attempts_left = attempts - attempt + 1
            if attempts_left == 1:
                print(f"{attempts_left} attempt left")
            else:
                print(f"{attempts_left} attempts left")
        elif guess == number:
            print(f"Congrats!! You guessed it in {attempt} attempts")
            player_score = level, name, attempt
            try:
                with open(file_name, "a") as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(player_score)
            except IOError:
                print("Could not write in file")
            break
    else:
        print(f"You ran out of attempts, the number was {number}")
    
def read_file(file_name):
    try:
        df = pd.read_csv(file_name)
        sorted_df = df.sort_values(by=["Level"], ascending=True)
        sorted_df.to_csv(file_name, index=False)
        if sorted_df.empty == False:
            print(sorted_df)
        else:
            print("Win to show your scores")
    except IOError:
        print("Could not read file")

def play_again():
    while True:
        try:
            again = input("Play again? Y or N: ")
            if again.lower() == "y":
                game_play()
                read_file(file_name)
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
    file_name = "player_scores.csv"

    create_file(file_name)
    game_title()
    player_name()
    game_play()
    read_file(file_name)
    play_again()