import json
from enums import ESide, EPiece

class Piece:

	with open('../config/mailBox.json') as mailBoxFile:
		tabs = json.load(mailBoxFile)
		
	tab120 = tabs.get("tab120")

	tab64 = tabs.get("tab64")


	#piece: EPiece
	#side: ESide
	#coord: number
	def __init__(self, side, coord, range, directions):
		self.side = side
		self.coord = coord
		self.firstMove = True
		self.range = range
		self.directions = directions

	def __str__(self): 
		return "Piece de type {0}, camp {1}, direction {2}, range {3}, coord {4}".format(type(self).__name__, self.side.name, self.directions, self.range, self.coord)

	def __repr__(self):
		return str(self) + "\n"

	"""
	occupiedCases:[
			"coord": piece (typeof Piece)
	]
	"""
	@staticmethod
	def isAllyPiece(mySide, occupiedCases, coord):
		piece = occupiedCases.get(coord)
		return True if (piece != None and piece.side == mySide) else False

	# See isAllyPiece
	@staticmethod
	def isEnemyPiece(mySide, occupiedCases, coord):
		piece = occupiedCases.get(coord)
		return True if (piece != None and piece.side != mySide) else False

	@staticmethod
	def isEmptyCase(occupiedCases, coord):
		return True if (occupiedCases.get(coord) == None) else False

	def coordsFromVector(self, moveVector):
		value64 = self.tab64[self.coord]
		return self.tab120[value64 + moveVector]

	def isOutOfBounds(self, moveVector): 
		coords = self.coordsFromVector(moveVector)
		if (coords == -1): return True
		return False

	def availableMoves(self, occupiedCases, lastMove):
		availableMoves = []
		for k in self.directions:
			for i in range(1, self.range + 1):
				if (self.isOutOfBounds(k*i)): break
				if (Piece.isAllyPiece(self.side, occupiedCases, self.coordsFromVector(k*i))): break
				if (Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(k*i))):
					availableMoves.append(self.coordsFromVector(k*i))
					break
				availableMoves.append(self.coordsFromVector(k*i))
		return availableMoves
		
	def move(self, occupiedCases, selectedMove, gameReview):
		gameReview.append([self.type, self.coord, selectedMove])

		# Capture a piece if the move is on a case occupied by an ennemy piece
		if self.isEnemyPiece(self.side, occupiedCases, selectedMove):
			del occupiedCases[selectedMove]

		# Move the selected piece to the selected case
		del occupiedCases[self.coord]
		self.coord = selectedMove
		occupiedCases[selectedMove] = self

		# The piece has moved, so if it's a pawn it cannot move by 2 square, and if it's a king or a rook it cannot rock anymore
		self.firstMove = False
		print(gameReview)
		return occupiedCases, gameReview