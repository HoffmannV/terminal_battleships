import os
import Color


class Game:
    x_axis = ["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    y_axis = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", "10 "]
    hit = "X"
    miss = "O"
    known_hits = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    known_misses = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    ship_positions = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    game_mode = {"single_player": 0, "local_coop": 1, "online": 2}
    difficulty = {"easy": 0, "normal": 1, "hard": 2}

    def __init__(self, ship_positions):
        self.draw_game_board()
        self.ship_positions.update(ship_positions)

    def start_game(self, difficulty, game_mode):
        pass

    def draw_game_board(self):
        os.system('cls')
        for element in self.x_axis:
            if element == "J":
                print(Color.Bg.black, element, Color.Bg.default)
            else:
                print(Color.Bg.black, element, end="")
        for element in self.y_axis:
            for i in range(len(self.x_axis)):
                if i == 0:
                    print(Color.Bg.black, element, end="")
                elif i < len(self.x_axis) - 1:
                    print(Color.Bg.blue, " ", end="")
                else:
                    print(Color.Bg.blue, " ", Color.Bg.default)

    def update_game_board(self, coordinates):
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
                if int(field.strip()) in self.known_hits[self.x_axis[i]]:
                    if i == len(self.x_axis) - 1:
                        print(Color.Bg.red, self.hit, Color.Bg.default)
                        continue
                    else:
                        print(Color.Bg.red, self.hit, Color.Bg.default, end="")
                        continue

                # check if the field is a known miss
                if int(field.strip()) in self.known_misses[self.x_axis[i]]:
                    if i == len(self.x_axis) - 1:
                        print(Color.Bg.light_grey, self.miss, Color.Bg.default)
                        continue
                    else:
                        print(Color.Bg.light_grey, self.miss, Color.Bg.default, end="")
                        continue

                # check if the field is a hit or a miss
                if field.strip() == y_coordinate and self.x_axis[i] == x_coordinate:
                    if int(field.strip()) in self.ship_positions[x_coordinate]:
                        if i == len(self.x_axis) - 1:
                            print(Color.Bg.red, self.hit, Color.Bg.default)
                            self.known_hits[x_coordinate].append(int(field.strip()))
                        else:
                            print(Color.Bg.red, self.hit, Color.Bg.default, end="")
                            self.known_hits[x_coordinate].append(int(field.strip()))
                    else:
                        if i == len(self.x_axis) - 1:
                            print(Color.Bg.light_grey, self.miss, Color.Bg.default)
                            self.known_misses[x_coordinate].append(int(field.strip()))
                        else:
                            print(Color.Bg.light_grey, self.miss, Color.Bg.default, end="")
                            self.known_misses[x_coordinate].append(int(field.strip()))
                    continue

                # if its not any of the above the field should be printed empty with a blue background color
                if i == len(self.x_axis) - 1:
                    print(Color.Bg.blue, " ", Color.Bg.default)
                else:
                    print(Color.Bg.blue, " ", Color.Bg.default, end="")