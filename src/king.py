from piece import Piece, EPiece, ESide

class King(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, 1, [ -10, 10, -1, 1, -11, -9, 11, 9 ])
    
    def availableMoves(self, occupiedCases):
        availableMoves = []
		#checks if rock is available when a king is selected
        if self.side == ESide.White:
            if self.firstMove:
                if not 61 in occupiedCases and not 62 in occupiedCases:
                    piece = occupiedCases.get(63)
                    if (piece != None and piece.firstMove):
                        availableMoves.append(62)
                if not 57 in occupiedCases and not 58 in occupiedCases and not 59 in occupiedCases:
                    piece = occupiedCases.get(56)
                    if (piece != None and piece.firstMove):
                        availableMoves.append(58)
        if self.side == ESide.Black:
            if self.firstMove:
                if not 5 in occupiedCases and not 6 in occupiedCases:
                    piece = occupiedCases.get(7)
                    if (piece != None and piece.firstMove):
                        availableMoves.append(6)
                if not 1 in occupiedCases and not 2 in occupiedCases and not 3 in occupiedCases:
                    piece = occupiedCases.get(0)
                    if (piece != None and piece.firstMove):
                        availableMoves.append(2)

        return availableMoves + super(King, self).availableMoves(occupiedCases)


        