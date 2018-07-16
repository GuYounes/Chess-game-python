import json
from enums.enums import ESide, EPiece

class Piece:

	"""
	{
	    "moves": {
			"pawn": {
				"white": {
					"direction": [-9, -10, -11, -20],
					"range": 1
				},
				"black": {
					"direction": [9, 10, 11, 20],
					"range": 1
				}
			},
			"rook": {
				"direction": [ -10, 10, -1, 1 ],
				"range": "7"
			},
			"bishop": {
				"direction": [ -11, -9, 11, 9 ],
				"range": 7
			},
	    }
	}
	"""
	with open('config/moves.json') as movesConfigFile:
	    moves = json.load(movesConfigFile).get("moves")

	with open('config/mailBox.json') as mailBoxFile:
		tabs = json.load(mailBoxFile)
		
	tab120 = tabs.get("tab120")

	tab64 = tabs.get("tab64")


	#piece: EPiece
	#side: ESide
	#coord: number
	def __init__(self, _type, side, coord):
		self.type = _type
		self.side = side
		self.coord = coord
		self.firstMove = True
		self.initRange()
		self.initDirection()

	def __str__(self): 
		return "Piece de type {0}, camp {1}, direction {2}, range {3}, coord {4}".format(self.type.name, self.side.name, self.directions, self.range, self.coord)

	def __repr__(self):
		return str(self) + "\n"

	# Initialize a new Piece with an object
	# {
	#     "coord": 1,
	#     "type": "bishop"
	# }
	@staticmethod
	def init(side, object):
		return Piece(EPiece[object.get("type").upper()], side, object.get("coord"))

	"""
	occupiedCases:[
			"piece": piece (typeof Piece)
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

	@staticmethod
	def removePieceFromCoord(occupiedCases, coord):
		if (occupiedCases.get(coord) != None):
			del occupiedCases[coord]

	def initRange(self):
		if (self.type == EPiece.PAWN):
			self.range = None
		else: 
			self.range = self.moves.get(self.type.name.lower()).get("range")

	def initDirection(self):
		if (self.type == EPiece.PAWN):
			self.directions = None
		else:  
			self.directions = self.moves.get(self.type.name.lower()).get("directions")

	def coordsFromVector(self, moveVector):
		value64 = self.tab64[self.coord]
		return self.tab120[value64 + moveVector]

	def isOutOfBounds(self, moveVector): 
		coords = self.coordsFromVector(moveVector)
		if (coords == -1): return True
		return False

	def transformation(self, newType):
		self.type = newType
		self.initRange()
		self.initDirection()

	def rock(self, selectedMove, occupiedCases):
		if self.type == EPiece.KING and self.firstMove:
			if self.side == ESide.WHITE:
				if selectedMove == 62:
					piece = occupiedCases.get(63)
					if piece != None and piece.firstMove:
						piece.move(occupiedCases, 61)
				if selectedMove == 58:
					piece = occupiedCases.get(56)
					if piece != None and piece.firstMove:
						piece.move(occupiedCases, 59)
			if self.side == ESide.BLACK:
				if selectedMove == 6:
					piece = occupiedCases.get(7)
					if piece != None and piece.firstMove:
						piece.move(occupiedCases, 5)
				if selectedMove == 2:
					piece = occupiedCases.get(0)
					if piece != None and piece.firstMove:
						piece.move(occupiedCases, 3)
		#checks if it's a rock move and move rooks if it the case

	def availableMoves(self, occupiedCases):
		availableMoves = []

		if(self.type == EPiece.PAWN):
			basicMove = -10 if self.side == ESide.WHITE else 10
			captureMove = [-11, -9] if self.side == ESide.WHITE else [11, 9]
			# If the case in front of the pawn is empty, it can move 
			if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove))):
				availableMoves.append(self.coordsFromVector(basicMove))
				# If the second case in front of the pawn is empty, it can move
				if (Piece.isEmptyCase(occupiedCases, self.coordsFromVector(basicMove*2)) and self.firstMove):
					availableMoves.append(self.coordsFromVector(basicMove*2))
			for move in captureMove:
				if ((not self.isOutOfBounds(move)) and (Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(move)))):
					availableMoves.append(self.coordsFromVector(move))
			return availableMoves
		#Pawns require a specific code because the way they capture is different from the other pieces, and they have a special move if they haven't move yet
		
		if(self.type == EPiece.KING):
			if self.side == ESide.WHITE:
				if self.firstMove:
					if not 61 in occupiedCases and not 62 in occupiedCases:
						piece = occupiedCases.get(63)
						if (piece != None and piece.firstMove):
							availableMoves.append(62)
					if not 57 in occupiedCases and not 58 in occupiedCases and not 59 in occupiedCases:
						piece = occupiedCases.get(56)
						if (piece != None and piece.firstMove):
							availableMoves.append(58)
			if self.side == ESide.BLACK:
				if self.firstMove:
					if not 5 in occupiedCases and not 6 in occupiedCases:
						piece = occupiedCases.get(7)
						if (piece != None and piece.firstMove):
							availableMoves.append(6)
					if not 1 in occupiedCases and not 2 in occupiedCases and not 3 in occupiedCases:
						piece = occupiedCases.get(0)
						if (piece != None and piece.firstMove):
							availableMoves.append(2)
		#checks if rock is available when a king is selected
				
		for k in self.directions:
			for i in range(1, self.range + 1):
				if (self.isOutOfBounds(k*i)): break
				if (Piece.isAllyPiece(self.side, occupiedCases, self.coordsFromVector(k*i))): break
				if (Piece.isEnemyPiece(self.side, occupiedCases, self.coordsFromVector(k*i))):
					availableMoves.append(self.coordsFromVector(k*i))
					break
				availableMoves.append(self.coordsFromVector(k*i))
		return availableMoves

	def move(self, occupiedCases, selectedMove):

		availableMoves = self.availableMoves(occupiedCases)

		if Piece.isEnemyPiece(self.side, occupiedCases, selectedMove):
			Piece.removePieceFromCoord(occupiedCases, selectedMove)
		#capture a piece if the move is on  a square occupied by an ennemy piece

		self.removePieceFromCoord(occupiedCases, self.coord)
		self.coord = selectedMove
		occupiedCases[selectedMove] = self
		#move the selected piece to the selected square

		self.rock(selectedMove, occupiedCases)

		self.firstMove = False
		#the piece has moved, so if it's a pawn it cannot move by 2 square, and if it's a king or a rook it cannot rock anymore

		if self.type == EPiece.PAWN and self.side == ESide.WHITE and self.coord < 8:
			self.transformation(EPiece.QUEEN)
		if self.type == EPiece.PAWN and self.side == ESide.BLACK and self.coord > 55:
			self.transformation(EPiece.QUEEN)
		#call the transformation function when a PAWN reaches the end of the chessboard

		print(occupiedCases)

