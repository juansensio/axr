from .board import Board

class Game():
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()

    def agent_move(self):
        return self.players[1].move(self.board)

    def is_game_over(self):
        return self.board.is_game_over()

    def reset(self):
        self.board.reset()

    def update(self, symbol, row, col):
        self.board.update(symbol, row, col)
