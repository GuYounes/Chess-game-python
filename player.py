import json
from piece import Piece
from enums.enums import ESide, EPiece

class Player:

	with open('config/pieces.json') as piecesConfigFile:
		piecesCoords = json.load(piecesConfigFile)

	# side: ESide
	def __init__(self, side):
		self.side = side
		self.initPiece()

	def initPiece(self):
		self.pieces = []
		for piece in self.piecesCoords.get(self.side.name.lower()):
			self.pieces.append(Piece.init(self.side, piece))

	def __str__(self):
		return "Player {0}, pieces: {1}".format(self.side.name, self.pieces)
