import random, os, csv

import pandas as pandasForSortingCSV

def game_title():
    print("Guess the Number Game")

def create_file(path, file_name):
    try:
        with open(path, file_name, "w") as f:
            f.write("Level,Player name,Attempts\n")
    except IOError:
        print("Could not create file")

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
    
    try:
        with open(path, file_name, "a") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([level, player_name, attempt])
    except IOError:
        print("Could not write in file")

def read_file(path, file_name):
    try:
        with open(path, file_name, "r") as f:
            panda_sorting = pandasForSortingCSV.read_csv(f)
            panda_sorting.sort_values(["Level"],
                               axis = 0,
                               ascending = [True],
                               inplace = True)
            print(panda_sorting)
    except IOError:
        print("Could not read file")

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
    path = r"E:\src"
    file_name = "scores.csv"

    create_file(file_name)
    game_title()
    player_name()
    game_play()
    read_file(file_name)
    play_again()