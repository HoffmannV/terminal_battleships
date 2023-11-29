class Player:
    ship_positions = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    known_hits = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    known_misses = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': []}
    difficulty_multiplier = {'Easy': 0.5, 'Normal': 1, 'Hard': 2}
    score = 0

    def __init__(self, ship_positions):
        self.ship_positions.update(ship_positions)

    def reset_ship_positions(self):
        for key in self.ship_positions.keys():
            self.ship_positions[key].clear()

    def full_reset(self):
        for key in self.ship_positions.keys():
            self.ship_positions[key].clear()

        for key in self.known_hits.keys():
            self.known_hits[key].clear()

        for key in self.known_misses.keys():
            self.known_misses[key].clear()

    def update_score(self, difficulty):
        positive = self.count_hits() * 20 * self.difficulty_multiplier[difficulty]
        negative = self.count_misses() * (-5) * self.difficulty_multiplier[difficulty]

        return positive + negative

    def count_hits(self):
        hits = 0

        for key in self.known_hits.keys():
            for hit in self.known_hits[key]:
                hits = hits + 1

        return hits

    def count_misses(self):
        misses = 0

        for key in self.known_misses.keys():
            for hit in self.known_misses[key]:
                misses = misses + 1

        return misses
