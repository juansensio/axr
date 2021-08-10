import pickle

class Agent():
    def __init__(self, value_function_path):
        with open(value_function_path, 'rb') as handle:
            self.value_function = pickle.load(handle)
        self.symbol = 1

    def move(self, board):
        valid_moves = board.valid_moves()
        # vamos a la posición con más valor
        max_value = -1000
        for row, col in valid_moves:
            next_board = board.state.copy()
            next_board[row, col] = self.symbol
            next_state = str(next_board.reshape(3*3))
            value = 0 if self.value_function.get(next_state) is None else self.value_function.get(next_state)
            if value >= max_value:
                max_value = value
                best_row, best_col = row, col
        return best_row, best_col
