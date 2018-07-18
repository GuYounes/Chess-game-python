from pieces.piece import Piece

class Queen(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 7, [ -10, 10, -1, 1, -11, -9, 11, 9 ])
