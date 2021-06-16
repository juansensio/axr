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

    def start(self):
        self.current_player = self.player1

    def update(self, y, x):
        # check valid
        if self.state[y][x] != 0:
            return False
        self.state[y][x] = self.current_player.marker
        self.current_player = self.player1 if self.current_player is self.player2 else self.player2
        return True

    def is_game_over(self):
        for fila in self.state:
            if fila[0] != 0 and fila[0] == fila[1] and fila[1] == fila[2]:
                return True
        for c in range(3):
            if self.state[0][c] != 0 and self.state[0][c] == self.state[1][c] and self.state[1][c] == self.state[2][c]:
                return True
        if self.state[0][0] != 0 and self.state[0][0] == self.state[1][1] and self.state[1][1] == self.state[2][2]:
            return True
        if self.state[0][2] != 0 and self.state[0][2] == self.state[1][1] and self.state[1][1] == self.state[2][0]:
            return True
        return False

    def reset(self):
        self.state = copy.deepcopy(self.initial_state)
