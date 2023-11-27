import os
import re

from Game import Game
from Player import Player

def load_logo():
    logo = """//      ____        __  __  __          __    _                 
//     / __ )____ _/ /_/ /_/ /__  _____/ /_  (_)___  _____      
//    / __  / __ `/ __/ __/ / _ \\/ ___/ __ \\/ / __ \\/ ___/   
//   / /_/ / /_/ / /_/ /_/ /  __(__  ) / / / / /_/ (__  )       
//  /_____/\\__,_/\\__/\\__/_/\\___/____/_/ /_/_/ .___/____/    
//                                         /_/                  
//"""
    print(logo)


def load_menu_options():
    menu_options = """//  ---Main Menu---
//
//  [S]tart game
//  [R]esume game
//  [M]ultiplayer
//  [E]xit
    """

    menu_option = input(menu_options)
    match menu_option.upper():
        case 'S':
            choose_game_difficulty()
        case 'R':
            pass
        case 'M':
            choose_multiplayer_game_mode()
        case 'E':
            exit()
        case _:
            os.system('cls')
            load_logo()
            print(wrong_option_chosen(menu_option))
            load_menu_options()


def choose_multiplayer_game_mode():
    os.system('cls')
    load_logo()
    multiplayer_options = """//  ---Multiplayer---
//
//  [S]plitscreen
//  [L]AN
//  [O]nline
//  [B]ack
    """

    multiplayer_option = input(multiplayer_options)
    match multiplayer_option.upper():
        case 'S':
            pass
        case 'L':
            pass
        case 'O':
            pass
        case 'B':
            os.system('cls')
            load_logo()
            load_menu_options()
        case _:
            os.system('cls')
            load_logo()
            print(wrong_option_chosen(multiplayer_option))
            choose_multiplayer_game_mode()


def choose_game_difficulty():
    os.system('cls')
    load_logo()
    difficulty_options = """//  ---Single Player---
//
//  [E]easy
//  [N]ormal
//  [H]ard
//  [T]est
//  [B]ack
    """

    difficulty_option = input(difficulty_options)
    match difficulty_option.upper():
        case 'E':
            pass
        case 'N':
            pass
        case 'H':
            pass
        case 'T':
            game, test_opponent = initialize_game()
            while test_opponent.known_hits != test_opponent.ship_positions:
                coordinates = input("Shoot your projectile: ")
                shooting_phase(coordinates, game, test_opponent)
        case 'B':
            os.system('cls')
            load_logo()
            load_menu_options()
        case _:
            os.system('cls')
            load_logo()
            print(wrong_option_chosen(difficulty_option))
            choose_game_difficulty()


def wrong_option_chosen(option):
    return "\tThe Option [{0}] does not exist! Try again!\n".format(option)


def shooting_phase(coordinates, game, test_opponent):
    match_string = "^[a-jA-J][1-9][0]?$"
    valid_coordinate = re.match(match_string, coordinates)

    if valid_coordinate:
        game.update_game_board(coordinates, test_opponent)
    else:
        new_coordinate = input("Not a valid coordinate. Please try again!\n")
        shooting_phase(new_coordinate, game, test_opponent)


def initialize_game():
    game = Game()
    test_ships = {'C': [1, 2, 3, 4, 5, 10], 'D': [10], 'E': [10], 'J': [2], 'I': [2], 'H': [2],
                  'G': [7, 8, 9, 2]}
    test_opponent = Player(test_ships)

    return game, test_opponent


if __name__ == '__main__':

    load_logo()
    load_menu_options()

    #Test game_update
    #game.update_game_board('c1', test_opponent)
    #game.update_game_board('c2', test_opponent)
    #game.update_game_board('c3', test_opponent)
    #game.update_game_board('j2', test_opponent)
    #game.update_game_board('c10', test_opponent)
    #game.update_game_board('h2', test_opponent)



