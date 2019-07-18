class Tile:
    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.current_piece = piece

    def is_occupied(self):
        return self.current_piece is not None