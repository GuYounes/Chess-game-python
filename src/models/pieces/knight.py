from pieces.piece import Piece

class Knight(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 1, [ -12, -21, -19, -8, 12, 21, 19, 8 ])
