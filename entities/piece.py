class Piece:
    def __init__(self, color):
        self.color = color
        self.is_alive = True

    def __repr__(self):
        life_str = "Dead" if self.is_alive else "Alive"
        return f"{self.color} piece, {life_str}"