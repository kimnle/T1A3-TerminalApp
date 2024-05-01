import csv
import random

import pandas as pd
from colored import Fore, Style


# Function prints game title
def game_title():
    print(f"{Fore.green}Guess the Number Game{Style.reset}")


# Function creates file and writes header
def create_file(file):
    try:
        with open(file, "w") as f:
            f.write("Level,Attempts\n")
    except IOError:
        print("Could not create file")


# Function asks for player's name
def player_name():
    while True:
        try:
            name = input("Player name: ")
            if not name:
                raise ValueError(f"{Fore.red}Cannot be empty{Style.reset}")
            else:
                print(f"Hey {Fore.blue}{name}{Style.reset}")
                break
        except ValueError as a:
            print(a)


# Function asks player if they want to play an easy, medium or hard game,
# generates a random number, asks for the player's guess,
# validates the guess, tracks the number of attempts and
# detects when the game is over.
# If the player wins, their score is appended to the file created earlier.
def game_play():
    while True:
        try:
            level = input(f"Choose level - {Fore.yellow}easy{Style.reset}, "
                          f"{Fore.dark_orange_3a}medium{Style.reset} or "
                          f"{Fore.light_red}hard{Style.reset}: ")
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
                raise ValueError(f"{Fore.red}Please type easy, medium or hard only"
                                 f"{Style.reset}")
        except ValueError as b:
            print(b)

    number = random.randint(1, max)
    attempt = 1

    while attempt <= attempts:
        while True:
            try:
                guess = int(input(f"Guess the number that I am thinking of from "
                                  f"{Fore.magenta}1{Style.reset} and {Fore.magenta}{max}{Style.reset}: "))
                if 1 <= guess <= max:
                    break
                else:
                    print(f"{Fore.red}Please enter a number between 1 and {max} inclusive"
                          f"{Style.reset}")
            except ValueError:
                    print(f"{Fore.red}Please enter numbers only{Style.reset}")

        if guess < number:
            print(f"{Fore.cyan}Higher{Style.reset}")
            attempt += 1
            attempts_left = attempts - attempt + 1
            if attempts_left == 1:
                print(f"{Fore.light_yellow}{attempts_left}{Style.reset} attempt left")
            else:
                print(f"{Fore.light_yellow}{attempts_left}{Style.reset} attempts left")
        elif guess > number:
            print(f"{Fore.light_green}Lower{Style.reset}")
            attempt += 1
            attempts_left = attempts - attempt + 1
            if attempts_left == 1:
                print(f"{Fore.light_yellow}{attempts_left}{Style.reset} attempt left")
            else:
                print(f"{Fore.light_yellow}{attempts_left}{Style.reset} attempts left")
        elif guess == number:
            print(f"{Fore.light_magenta}Congrats!!{Style.reset} You guessed it in "
                  f"{Fore.light_yellow}{attempt}{Style.reset} attempts")
            score = level, attempt
            try:
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(score)
            except IOError:
                print("Could not write in file")
            break

    else:
        print(f"{Fore.purple_4a}You ran out of attempts, the number was{Style.reset} "
              f"{number}")


# Function sorts and reads the .csv file with Python pandas
def read_file(file):
    try:
        df = pd.read_csv(file)
        sorted_df = df.sort_values(by=["Level"], ascending=True)
        sorted_df.to_csv(file, index=False)
        if sorted_df.empty == False:
            print("Your scores")
            print(sorted_df)
        else:
            print("Win to show your scores")
    except IOError:
        print("Could not read file")


# Function asks player if they want to play again
def play_again():
    while True:
        try:
            again = input(f"{Fore.dark_sea_green_4a}Play again?{Style.reset} Y or N: ")
            if again.lower() == "y":
                game_play()
                read_file(file)
                play_again()
                break
            elif again.lower() == "n":
                print(f"Play again {Fore.pale_turquoise_4}soon{Style.reset}!!")
                break
            else:
                raise ValueError(f"{Fore.red}Please type Y or N only{Style.reset}")
        except ValueError as c:
            print(c)


if __name__ == "__main__":
    file = "player_scores.csv"

    create_file(file)
    game_title()
    player_name()
    game_play()
    read_file(file)
    play_again()