import json
from pieces.king import King, ESide
from pieces.knight import Knight
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.pawn import Pawn

class Player:

    with open('../../config/pieces.json') as piecesConfigFile:
        piecesCoords = json.load(piecesConfigFile)

    # side: ESide
    def __init__(self, side):
        self.side = side
        self.initPiece()

    def initPiece(self):
        self.pieces = []
        for piece in self.piecesCoords.get(self.side.name.lower()):
            function = getattr(Player, piece.get("type"))
            p = function(self, self.side, piece.get("coord"))
            self.pieces.append(p)

    def knight(self, side, coord):
        return Knight(side, coord)

    def queen(self, side, coord):
        return Queen(side, coord)
    
    def king(self, side, coord):
        return King(side, coord)

    def bishop(self, side, coord):
        return Bishop(side, coord)
        
    def pawn(self, side, coord):
        return Pawn(side, coord)
    
    def rook(self, side, coord):
        return Rook(side, coord)

    def __str__(self):
        return "Player {0}, pieces: {1}".format(self.side.name, self.pieces)

