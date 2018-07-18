from pieces.piece import Piece

class Bishop(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 7, [ -11, -9, 11, 9 ])
