import copy


class Board():
    def __init__(self, player1, player2):
        self.initial_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.player1 = player1
        self.player2 = player2
        self.current_player = self.player1
        self.state = copy.deepcopy(self.initial_state)

    def update(self, y, x):
        # check valid
        if self.state[y][x] != 0:
            return False
        self.state[y][x] = self.current_player.marker
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2
        return True

    def is_game_over(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    count += 1
        return count == 0

    def reset(self):
        self.state = copy.deepcopy(self.initial_state)
