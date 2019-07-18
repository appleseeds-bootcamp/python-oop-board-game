from entities.checkers.checkers_piece import CheckersPiece

class CheckersGameBoard(GameBoard):
    def __init__(self):
        super().__init__(8, 8)
        self._pose_checkers_pieces()

    def _pose_checkers_pieces(self):
        for i in range(len(self.board)):
            for j in range(2):
                board[i][j].current_piece = CheckersPiece("white")

            for j in range(6, 8):
                board[i][j].current_piece = CheckersPiece("black")
