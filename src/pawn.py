from piece import Piece, EPiece, ESide
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook

class Pawn(Piece):

	def __init__(self, side, coord):
		super().__init__(side, coord, None, [])
		self.type = 'pawn'
	
	def availableMoves(self, occupiedCases, lastMove):#lastMove is an array: [type, before move square, after move square]
		availableMoves = []

		#Pawns require a specific code because the way they capture is different from the other pieces, and they have a special move if they haven't move yet
		basicMove = -10 if self.side == ESide.White else 10
		captureMove120 = [-11, -9] if self.side == ESide.White else [11, 9]
		captureMove64 = [-9, -7] if self.side == ESide.White else [7, 9]
		# If the case in front of the pawn is empty, it can move 
		if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove))):
			availableMoves.append(self.coordsFromVector(basicMove))
			# If the second case in front of the pawn is empty, it can move
			if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove*2)) and self.firstMove):
				availableMoves.append(self.coordsFromVector(basicMove*2))
		#for capture and en passant
		for move120 in captureMove120:
			if (not self.isOutOfBounds(move120)):
				#for capture
				if Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(move120)):
			   		availableMoves.append(self.coordsFromVector(move120))
			   	#for en passant
				for move64 in captureMove64:
					if self.side == ESide.White and 23 < self.coord < 32 or self.side == ESide.Black and 31 < self.coord < 40:
						enPassantPawnCoord = move64 + 8 + self.coord if self.side == ESide.White else move64 - 8 + self.coord
						if Piece.isEnemyPiece(self.side, occupiedCases, enPassantPawnCoord):
							if lastMove[0] == 'pawn' and lastMove[2] == enPassantPawnCoord and abs(lastMove[2] - lastMove[1]) == 16:
								availableMoves.append(self.coord + move64)								
		return availableMoves

 	# Transform the PAWN when it reaches the end of the chessboard
	def promotion(self, newType, occupiedCases):
		if ((self.side == ESide.White and self.coord < 8) or (self.side == ESide.Black and self.coord > 55 )):
			if (newType == "Queen"):
				occupiedCases[self.coord] = Queen(self.side, self.coord)
		return occupiedCases

	# Remove a pawn when a en passant move is used
	def removeEnPassantPawn(self, occupiedCases,selectedMove):
		if self.side == ESide.White and 23 < self.coord < 32 or self.side == ESide.Black and 31 < self.coord < 40:
			if abs(selectedMove - self.coord) in [7, 9]: #very specific case, disallow the pawn to delete himself when he moves forward after not taking an opportunity of en passant
				if Piece.isEmptyCase(occupiedCases, selectedMove): #check if the move is on an empty case, so it makes sure it's en passant
					enPassantPawnCoord = selectedMove + 8 if self.side == ESide.White else selectedMove - 8
					del occupiedCases[enPassantPawnCoord]
		return occupiedCases

	def move(self, occupiedCases, selectedMove, gameReview):
		occupiedCases = self.removeEnPassantPawn(occupiedCases, selectedMove)
		super(Pawn, self).move(occupiedCases, selectedMove, gameReview)
		self.promotion("Queen", occupiedCases)
		return occupiedCases, gameReview


