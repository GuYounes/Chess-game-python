from piece import Piece, EPiece

class Rook(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 7, [ -10, 10, -1, 1 ])
        self.type = EPiece.Rook