from piece import Piece, EPiece, ESide
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook

class Pawn(Piece):

    def __init__(self, side, coord):
        super().__init__(side, coord, None, [])
        self.enPassant = True
    
    def availableMoves(self, occupiedCases):
        availableMoves = []
        #Pawns require a specific code because the way they capture is different from the other pieces, and they have a special move if they haven't move yet
        
        basicMove = -10 if self.side == ESide.White else 10
        captureMove = [-11, -9] if self.side == ESide.White else [11, 9]
        # If the case in front of the pawn is empty, it can move 
        if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove))):
            availableMoves.append(self.coordsFromVector(basicMove))
            # If the second case in front of the pawn is empty, it can move
            if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove*2)) and self.firstMove):
                availableMoves.append(self.coordsFromVector(basicMove*2))
        for move in captureMove:
            if (not self.isOutOfBounds(move)):
                if Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(move)):
               	    availableMoves.append(self.coordsFromVector(move))
                if self.side == ESide.White and 23 < self.coord < 32 or self.side == ESide.Black and 31 < self.coord < 40:
                	enPassantPawnCoord = move + 10 if self.side == ESide.White else move - 10
                	if Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(enPassantPawnCoord)):
                		if occupiedCases[enPassantPawnCoord + self.coord].enPassant:
                			availableMoves.append(self.coordsFromVector(move))
        return availableMoves

 	# Transform the PAWN when it reaches the end of the chessboard
    def promotion(self, newType, occupiedCases):
        if ((self.side == ESide.White and self.coord < 8) or (self.side == ESide.Black and self.coord > 55)):
            if (newType == "Queen"):
               occupiedCases[self.coord] = Queen(self.side, self.coord)
        return occupiedCases
'''
def movepawn(self, occupiedCases, selectedMove):
    super(Pawn, self).move(occupiedCases, selectedMove)
    self.promotion("Queen", occupiedCases)
'''