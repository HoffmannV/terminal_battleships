import os
import random

import Color
from Ship import Ship


def find_next_key(dictionary, key):
    next_key = ''
    found_current_key = False

    for dict_key in dictionary.keys():
        if found_current_key:
            next_key = dict_key
            break
        if dict_key == key:
            found_current_key = True
            next_key = dict_key
    return next_key


def find_prev_key(dictionary, key):
    prev_key = 'A'

    for dict_key in dictionary.keys():
        if dict_key == key:
            break
        prev_key = dict_key

    return prev_key


class Game:
    x_axis = ["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    y_axis = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", "10 "]
    hit = "X"
    miss = "O"
    game_mode = {"single_player": 0, "local_coop": 1, "online": 2}
    difficulty = {"easy": 0, "normal": 1, "hard": 2}
    ships = [Ship("Carrier", 5), Ship("Battleship", 4), Ship("Cruiser", 3), Ship("Submarine", 3), Ship("Destroyer", 2)]

    def __init__(self):
        self.draw_game_board()

    def start_game(self, difficulty, game_mode):
        pass

    def draw_game_board(self):
        os.system('cls')
        for element in self.x_axis:
            if element == "J":
                print(Color.Bg.black, element, Color.Bg.default)
            else:
                print(Color.Bg.black, element, Color.Bg.default, end="")
        for element in self.y_axis:
            for i in range(len(self.x_axis)):
                if i == 0:
                    print(Color.Bg.black, element, Color.Bg.default, end="")
                elif i < len(self.x_axis) - 1:
                    print(Color.Bg.blue, " ", Color.Bg.default, end="")
                else:
                    print(Color.Bg.blue, " ", Color.Bg.default)

    def preview_game_board(self, player):
        # draw header
        for field in self.x_axis:
            if field == "J":
                print(Color.Bg.black, field, Color.Bg.default)
            else:
                print(Color.Bg.black, field, Color.Bg.default, end="")

        # draw rows
        for field in self.y_axis:
            for i in range(len(self.x_axis)):

                # draw first field in row it should be a number with a black background
                if i == 0:
                    print(Color.Bg.black, field, end="")
                    continue

                # check if the field is a ship position
                if int(field.strip()) in player.ship_positions[self.x_axis[i]]:
                    if i == len(self.x_axis) - 1:
                        print(Color.Bg.green, " ", Color.Bg.default)
                        continue
                    else:
                        print(Color.Bg.green, " ", Color.Bg.default, end="")
                        continue

                # if it's not any of the above the field should be printed empty with a blue background color
                if i == len(self.x_axis) - 1:
                    print(Color.Bg.blue, " ", Color.Bg.default)
                else:
                    print(Color.Bg.blue, " ", Color.Bg.default, end="")

    def update_game_board(self, coordinates, opponent_player):
        os.system('cls')
        x_coordinate = coordinates[0].upper()
        y_coordinate = coordinates[1:]

        # draw header opponent
        print(Color.Bg.cyan, "Opponent: ", Color.Bg.default)

        # draw header
        for field in self.x_axis:
            if field == "J":
                print(Color.Bg.black, field, Color.Bg.default)
            else:
                print(Color.Bg.black, field, Color.Bg.default, end="")

        # draw rows
        for field in self.y_axis:
            for i in range(len(self.x_axis)):

                # draw first field in row it should be a number with a black background
                if i == 0:
                    print(Color.Bg.black, field, end="")
                    continue

                # check if the field is a known hit
                if int(field.strip()) in opponent_player.known_hits[self.x_axis[i]]:
                    if i == len(self.x_axis) - 1:
                        print(Color.Bg.red, self.hit, Color.Bg.default)
                        continue
                    else:
                        print(Color.Bg.red, self.hit, Color.Bg.default, end="")
                        continue

                # check if the field is a known miss
                if int(field.strip()) in opponent_player.known_misses[self.x_axis[i]]:
                    if i == len(self.x_axis) - 1:
                        print(Color.Bg.light_grey, self.miss, Color.Bg.default)
                        continue
                    else:
                        print(Color.Bg.light_grey, self.miss, Color.Bg.default, end="")
                        continue

                # check if the field is a hit or a miss
                if field.strip() == y_coordinate and self.x_axis[i] == x_coordinate:
                    if int(field.strip()) in opponent_player.ship_positions[x_coordinate]:
                        if i == len(self.x_axis) - 1:
                            print(Color.Bg.red, self.hit, Color.Bg.default)
                            opponent_player.known_hits[x_coordinate].append(int(field.strip()))
                        else:
                            print(Color.Bg.red, self.hit, Color.Bg.default, end="")
                            opponent_player.known_hits[x_coordinate].append(int(field.strip()))
                    else:
                        if i == len(self.x_axis) - 1:
                            print(Color.Bg.light_grey, self.miss, Color.Bg.default)
                            opponent_player.known_misses[x_coordinate].append(int(field.strip()))
                        else:
                            print(Color.Bg.light_grey, self.miss, Color.Bg.default, end="")
                            opponent_player.known_misses[x_coordinate].append(int(field.strip()))
                    continue

                # if it's not any of the above the field should be printed empty with a blue background color
                if i == len(self.x_axis) - 1:
                    print(Color.Bg.blue, " ", Color.Bg.default)
                else:
                    print(Color.Bg.blue, " ", Color.Bg.default, end="")

    def place_ships_random(self, player):
        tmp_x_axis = self.x_axis[1:]
        tmp_y_axis = [int(y.strip()) for y in self.y_axis]
        possible_positions = {}

        # clear preloaded ship positions
        player.reset_ship_postions()

        for x in tmp_x_axis:
            possible_positions.update({x: [y for y in tmp_y_axis]})

        # iterate over the ships in the array
        for ship in self.ships:
            failed = True

            # random placement
            while failed:
                dict_entries_to_remove = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [],
                                          'I': [], 'J': []}
                # define a random starting point
                x_coordinate = random.choice(list(possible_positions.keys()))
                y_coordinate = random.choice(possible_positions[x_coordinate])
                dict_entries_to_remove[x_coordinate].append(y_coordinate)
                # possible_positions[x_coordinate].pop(possible_positions[x_coordinate].index(y_coordinate))

                # player.ship_positions.update({x_coordinate: y_coordinate})

                # decide on ship orientation 0 for horizontal 1 for vertical
                orientation = random.choice([0, 1])

                next_key = find_next_key(possible_positions, x_coordinate)
                prev_key = find_prev_key(possible_positions, x_coordinate)
                if y_coordinate == 10:
                    up_field = 0
                else:
                    up_field = y_coordinate - 1
                if y_coordinate == 0:
                    down_field = 10
                else:
                    down_field = y_coordinate + 1

                # decide on the initial direction
                direction = random.choice([0, 1])

                for i in range(ship.length - 1):
                    if orientation == 1:
                        # check if the right adjacent field is already occupied

                        if y_coordinate in possible_positions[next_key] and not x_coordinate == next_key \
                                and not (y_coordinate in dict_entries_to_remove[next_key]):
                            x_coordinate = next_key
                            next_key = find_next_key(possible_positions, x_coordinate)
                            # player.ship_positions.update({x_coordinate: y_coordinate})
                            dict_entries_to_remove[x_coordinate].append(y_coordinate)
                            # possible_positions[x_coordinate].pop(
                            #    possible_positions[x_coordinate].index(y_coordinate))
                            failed = False

                        elif not x_coordinate == prev_key and y_coordinate in possible_positions[prev_key] \
                                and not (y_coordinate in dict_entries_to_remove[prev_key]):
                            x_coordinate = prev_key
                            prev_key = find_prev_key(possible_positions, x_coordinate)
                            # player.ship_positions.update({x_coordinate: y_coordinate})
                            dict_entries_to_remove[x_coordinate].append(y_coordinate)
                            # possible_positions[x_coordinate].pop(
                            #    possible_positions[x_coordinate].index(y_coordinate))
                            failed = False

                        else:
                            dict_entries_to_remove.clear()
                            failed = True

                    elif orientation == 0:
                        if y_coordinate in possible_positions[x_coordinate] and not y_coordinate == up_field \
                                and not (up_field in dict_entries_to_remove[x_coordinate]):
                            y_coordinate = up_field
                            if y_coordinate == 10:
                                up_field = 0
                            else:
                                up_field = y_coordinate - 1
                            # player.ship_positions.update({x_coordinate: y_coordinate})
                            dict_entries_to_remove[x_coordinate].append(y_coordinate)
                            # possible_positions[x_coordinate].pop(
                            #    possible_positions[x_coordinate].index(y_coordinate))
                            failed = False

                        elif not y_coordinate == down_field and y_coordinate in possible_positions[x_coordinate] \
                                and not (up_field in dict_entries_to_remove[x_coordinate]):
                            y_coordinate = down_field
                            if y_coordinate == 10:
                                down_field = 0
                            else:
                                down_field = y_coordinate + 1
                            # player.ship_positions.update({x_coordinate: y_coordinate})
                            dict_entries_to_remove[x_coordinate].append(y_coordinate)
                            # possible_positions[x_coordinate].pop(
                            #    possible_positions[x_coordinate].index(y_coordinate))
                            failed = False

                        else:
                            dict_entries_to_remove.clear()
                            failed = True

                # print(possible_positions)
                if not failed:
                    for key in dict_entries_to_remove.keys():
                        for item in dict_entries_to_remove[key]:
                            if item in player.ship_positions[key] and not (item in possible_positions[key]):
                                failed = True
                            else:
                                player.ship_positions[key].append(item)
                                # print("Key: {0}, Item: {1}".format(key, possible_positions[key]))
                                possible_positions[key].pop(possible_positions[key].index(item))
                dict_entries_to_remove.clear()

        # Prints the ship positions for testing purposes
        # print(player.ship_positions)
