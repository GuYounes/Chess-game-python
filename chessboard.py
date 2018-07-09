import json
from player import Player

class ChessBoard:

	with open('config/mailBox.json') as mailBoxFile:
		tabs = json.load("mailBoxFile")
		tab120 = tabs.get("tab120")
		tab64 = tabs.get("tab64")

	def __init__(self):
		self.playerWhite = Player(ESide.WHITE)
		self.playerBlack = Player(ESide.BLACK)

	def __str__(self):
		return "Player white: {0}, Player black: {1}".format(self.playerWhite, self.playerBlack)



print(tabs)



