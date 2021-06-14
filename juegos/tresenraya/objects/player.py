class Player():
    def __init__(self, marker):
        if marker != 'X' and marker != 'O':
            raise ValueError("marker should be one of `X` or `O` ")
        self.marker = marker
