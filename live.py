import MemoryGame
import GuessGame
import CurrencyRouletteGame
import time


def welcome():
    name = input("Please enter your name: ")
    str1 = "Hello "
    str2 = " and welcome to the World of Games."
    "Here you can find many cool games to play."
    return str1 + name + str2


def load_game():
    flag = True
    while flag:
        list_of_games = [MemoryGame, GuessGame, CurrencyRouletteGame]
        with open("games.txt") as f:
            print(f.read())
        game_choice = int(input("Please choose your game 1-3: "))
        difficulty = int(input("Please choose difficulty 1-5: "))
        if 0 < game_choice < 4 and 0 < difficulty < 6:
            result = list_of_games[game_choice - 1].play(difficulty)
            print(result)
            flag = False
        else:
            print("Sorry, your choice is out of range, try again")
            time.sleep(1.5)
