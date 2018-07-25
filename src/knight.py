from piece import Piece, EPiece

class Knight(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 1, [ -12, -21, -19, -8, 12, 21, 19, 8 ])
        self.type = EPiece.Knight
