from enum import Enum

class ESide(Enum):
	White = 1
	Black = 2
	Neutral = 3

class EPiece(Enum):
	Pawn = 1
	Rook = 2
	Bishop = 3
	Knight = 4
	Queen = 5
	King = 6