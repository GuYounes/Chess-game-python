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

	number = 10

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

	def removePieceFromCoord(self, occupiedCases, coord):
		index = self.retrievePieceIndexFromCoord(occupiedCases, coord)
		del occupiedCases[index]

	def retrievePieceIndexFromCoord(self, occupiedCases, coord):
		for k in range(0, len(occupiedCases)):
			piece = occupiedCases[k]
			if (piece.coord == coord):
				return k
		return -1

	def transformation(self, piece, newType):
		piece.type == newType
		self.initRange()
		self.initDirection()


	"""
	occupiedCases:[
			"piece": piece (typeof Piece)
	]
	"""
	def isAllyPiece(self, occupiedCases, coord):
		for piece in occupiedCases:
			if (piece.coord == coord):
				if (piece.side == self.side):
					return True
		return False

	# See isAllyPiece
	def isEnemyPiece(self, occupiedCases, coord):
		for piece in occupiedCases:
			if (piece.coord == coord):
				if (piece.side != self.side):
					return True
		return False

	def availableMoves(self, occupiedCases):
		availableMoves = []

		if(self.type == EPiece.PAWN): return

		for k in self.directions:
			for i in range(1, self.range + 1):
				if (self.isOutOfBounds(k*i)): break
				if (self.isAllyPiece(occupiedCases, self.coordsFromVector(k*i))): break
				if (self.isEnemyPiece(occupiedCases, self.coordsFromVector(k*i))):
					availableMoves.append(self.coordsFromVector(k*i))
					break
				availableMoves.append(self.coordsFromVector(k*i))
		return availableMoves

	def move(self, occupiedCases, selectedMove):
		availableMoves = self.availableMoves(occupiedCases)
		if not selectedMove in availableMoves:
			print("This move is not correct")
		else:
			if self.isEnemyPiece(occupiedCases, selectedMove):
				self.removePieceFromCoord(occupiedCases, selectedMove)
			self.coord = selectedMove




