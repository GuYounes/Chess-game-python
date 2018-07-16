from player import Player
from enums.enums import ESide

class ChessBoard:

	def __init__(self):
		self.playerWhite = Player(ESide.WHITE)
		self.playerBlack = Player(ESide.BLACK)
		self.initOccupiedCases()

	def __str__(self):
		return "Player white: {0}, Player black: {1}".format(self.playerWhite, self.playerBlack)

	def initOccupiedCases(self):
		self.occupiedCases = {}
		for piece in self.playerWhite.pieces:
			self.occupiedCases[piece.coord] = piece

		for piece in self.playerBlack.pieces:
			self.occupiedCases[piece.coord] = piece

	

