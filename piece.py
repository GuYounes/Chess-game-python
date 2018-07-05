import json
from enums.enums import ESide, EPiece

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

class Piece:

	#piece: EPiece
	#side: ESide
	#coord: number
	def __init__(self, piece, side, coord):
		self.piece = piece
		self.side = side
		self.coord = coord
		self.initRange()
		self.initDirection()

	def __str__(self): 
		return "Piece de type {0}, camp {1}, direction {2}, range {3}".format(self.piece.name, self.side.name, self.direction, self.range)

	def __repr__(self):
		return str(self) + "\n";

	def initRange(self):
		if (self.piece == EPiece.PAWN):
			self.range = moves.get(self.piece.name.lower()).get(self.side.name.lower()).get("range");
		else: 
			self.range = moves.get(self.piece.name.lower()).get("range");

	def initDirection(self):
		if (self.piece == EPiece.PAWN):
			self.direction = moves.get(self.piece.name.lower()).get(self.side.name.lower()).get("direction");
		else:  
			self.direction = moves.get(self.piece.name.lower()).get("direction");

	# Initialize a new Piece with an object
	# {
	#     "coord": 1,
	#     "type": "bishop"
	# }
	def init(side, object):
		return Piece(EPiece[object.get("type").upper()], side, object.get("coord"))

