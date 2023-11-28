class Player:
    ship_positions = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    known_hits = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    known_misses = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}

    def __init__(self, ship_positions):
        self.ship_positions.update(ship_positions)

    def reset_ship_postions(self):
        for key in self.ship_positions.keys():
            self.ship_positions[key].clear()

    def full_reset(self):
        for key in self.ship_positions.keys():
            self.ship_positions[key].clear()

        for key in self.known_hits.keys():
            self.known_hits[key].clear()

        for key in self.known_misses.keys():
            self.known_misses[key].clear()
