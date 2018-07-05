from enum import Enum

class ESide(Enum):
	WHITE = 1
	BLACK = 2
	NEUTRAL = 3

class EPiece(Enum):
	PAWN = 1
	ROOK = 2
	BISHOP = 3
	KNIGHT = 4
	QUEEN = 5
	KING = 6