from enum import Enum

class ESide(Enum):
	White = 0
	Black = 1
	Neutral = 2

class EPiece(Enum):
	Pawn = 0
	Rook = 1
	Bishop = 2
	Knight = 3
	Queen = 4
	King = 5