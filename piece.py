import json
from enum import Enum
from white import ESide

with open('config/moves.json') as movesConfigFile:
    moves = json.load(movesConfigFile).get("moves")

class EPiece(Enum):
	PAWN = 1
	ROOK = 2
	BISHOP = 3
	KNIGHT = 4
	QUEEN = 5
	KING = 6

class Piece:

	def __init__(self, piece, side):
		self.piece = piece
		self.side = side
		self.initRange()
		self.initDirection()

	def __str__(self): 
		return "Pice de type {0}, camp {1}, direction {2}, range {3}".format(self.piece.name, self.side.name, self.direction, self.range)

	def initRange(self):
		self.range = moves.get(self.piece.name.lower()).get("range");

	def initDirection(self):
		self.direction = moves.get(self.piece.name.lower()).get("direction");


piece = Piece(EPiece.ROOK, ESide.WHITE)
print(piece)
print(moves)
