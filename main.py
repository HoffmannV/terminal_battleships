import os
import re
import time
import platform

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


def return_to_menu_countdown(time_in_sec):
    print("Returning to the main menu in ", end="")
    for i in range(1, time_in_sec):
        print("{0}... ".format(10 - i), end="")
        time.sleep(1)
    print("\n")


def clear_screen():
    operating_system = platform.system()
    if operating_system == 'Linux':
        os.system('clear')
    else:
        os.system('cls')


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
            choose_single_player_mode()
        case 'R':
            pass
        case 'M':
            choose_multiplayer_game_mode()
        case 'E':
            exit()
        case _:
            clear_screen()
            load_logo()
            print(wrong_option_chosen(menu_option))
            load_menu_options()


def choose_multiplayer_game_mode():
    clear_screen()
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
            clear_screen()
            load_logo()
            load_menu_options()
        case _:
            clear_screen()
            load_logo()
            print(wrong_option_chosen(multiplayer_option))
            choose_multiplayer_game_mode()


def choose_single_player_mode():
    clear_screen()
    load_logo()
    difficulty_options = """//  ---Single Player---
//
//  [S]olo
//  [K]I
//  [T]est
//  [B]ack
    """

    difficulty_option = input(difficulty_options)
    match difficulty_option.upper():
        case 'S':
            choose_solo_difficulty()
        case 'K':
            pass
        case 'T':
            game, test_opponent = initialize_game()
            while test_opponent.known_hits != test_opponent.ship_positions:
                coordinates = input("Shoot your projectile: ")
                shooting_phase(coordinates, game, test_opponent)
        case 'B':
            clear_screen()
            load_logo()
            load_menu_options()
        case _:
            clear_screen()
            load_logo()
            print(wrong_option_chosen(difficulty_option))
            choose_single_player_mode()


def choose_solo_difficulty():
    clear_screen()
    load_logo()
    difficulty_options = """//  ---Single Player---
//
//  [E]asy
//  [N]ormal
//  [H]ard
//  [B]ack
"""
    difficulty_option = input(difficulty_options)
    match difficulty_option.upper():
        case 'E':
            solo_game_mode('Easy')
        case 'N':
            solo_game_mode('Normal')
        case 'H':
            solo_game_mode('Hard')
        case 'B':
            clear_screen()
            load_logo()
            load_menu_options()
        case _:
            clear_screen()
            load_logo()
            print(wrong_option_chosen(difficulty_option))
            choose_solo_difficulty()


def wrong_option_chosen(option):
    return "\tThe Option [{0}] does not exist! Try again!\n".format(option)


def shooting_phase(coordinates, game, test_opponent):
    match_string = "^[a-jA-J][1-9][0]?$"
    valid_coordinate = re.match(match_string, coordinates)

    if valid_coordinate:
        clear_screen()
        game.update_game_board(coordinates, test_opponent)
    else:
        new_coordinate = input("Not a valid coordinate. Please try again!\n")
        shooting_phase(new_coordinate, game, test_opponent)


def draw_score_board(player, difficulty=1):
    print("Hits: {0}\t\tMisses: {1}".format(player.count_hits(), player.count_misses()))
    print("Score: {0}".format(player.update_score(difficulty)))


def initialize_game():
    game = Game()
    test_ships = {'A': [], 'B': [10], 'C': [10], 'D': [10], 'E': [10, 6, 7, 8], 'F': [10, 2, 3, 4, 9], 'G': [],
                  'H': [], 'I': [3, 4], 'J': [6, 7, 8, 9]}
    test_opponent = Player(test_ships)

    return game, test_opponent


def solo_game_mode(difficulty):
    clear_screen()
    show_opponent_ship_positions = False
    game, test_opponent = initialize_game()
    game.place_ships_random(test_opponent)
    while not test_opponent.known_hits == test_opponent.ship_positions:
        coordinates = input("Shoot your projectile: ")

        if coordinates == "enable cheats":
            show_opponent_ship_positions = True
            print("Showing enemy ship positions")
            print(test_opponent.ship_positions)
            coordinates = input("Shoot your projectile: ")
        elif coordinates == "disable cheats":
            show_opponent_ship_positions = False
            print("Disabled showing enemy ship positions")
            coordinates = input("Shoot your projectile: ")

        shooting_phase(coordinates, game, test_opponent)
        if show_opponent_ship_positions is True:
            print(test_opponent.ship_positions)
        draw_score_board(test_opponent, difficulty)

    print("    ---Game-over!---    ")
    print("    ----You-won!---     \n")
    print("Returning to the main menu in ", end="")
    for i in range(1, 10):
        print("{0}... ".format(10 - i), end="")
        time.sleep(1)
    print("\n")

    load_logo()
    load_menu_options()


if __name__ == '__main__':
    load_logo()
    load_menu_options()

    # Test game_update
    # game.update_game_board('c1', test_opponent)
    # game.update_game_board('c2', test_opponent)
    # game.update_game_board('c3', test_opponent)
    # game.update_game_board('j2', test_opponent)
    # game.update_game_board('c10', test_opponent)
    # game.update_game_board('h2', test_opponent)
