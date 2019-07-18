from entities.piece import Piece

class CheckersPiece(Piece):
    def __init__(self, color):
        super().__init__(color)

        self.is_king = False
