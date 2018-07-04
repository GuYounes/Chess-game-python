from enum import Enum

class ESide(Enum):
	WHITE = 1
	BLACK = 2
	NEUTRAL = 3

class Player:

	def __init__(self, side):
		self.side = side
