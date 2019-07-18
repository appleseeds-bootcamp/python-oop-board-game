from entities.tile import Tile

class GameBoard:
    def __init__(self, height, width):
        self.board = self.__create_board(height, width)

    def __create_board(self, height, width):
        board = []
        for i in range(height):
            board.append([])
            for j in range(width):
                board[i].append(Tile(i, j))
        
        return board