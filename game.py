import pygame as pg
from chessboard import ChessBoard, ESide
from piece import Piece
from enums.enums import EPiece
from images import * 
from settings import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTHDISPLAY, HEIGHTDISPLAY))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.turn = ESide.WHITE
		self.currentPiece = None
		self.new()

	def new(self):
		self.initDraw()
		self.grid = self.getAndDrawGrid() #The key to transit between coords and the screen
		self.chessboard = ChessBoard()
		self.run()

	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.draw()

	def events(self):
		for event in pygame.event.get():
			click = pg.mouse.get_pressed()

			if event.type == pg.QUIT:
				pg.quit()
				quit()
		
			self.pointedSquare = self.retrieveCoordFromMouseIfAvailable()
			
			if click[0] == 1:
				print(self.pointedSquare)
				if (self.currentPiece != None and self.currentPiece.coord == self.pointedSquare):
					pass
				elif (self.pointedSquare != -1):
					self.onAvailableCaseClick()
				else:
					self.currentPiece = None
					print("deselect piece")

	def onAvailableCaseClick(self): 
		if (self.currentPiece != None):
			self.currentPiece.move(self.chessboard.occupiedCases, self.pointedSquare)
			self.switchTurn()
			self.currentPiece = None
		else :
			pieceIndex = Piece.retrievePieceIndexInOccupiedCasesFromCoord(self.chessboard.occupiedCases, self.pointedSquare)
			if (pieceIndex != -1):
				self.currentPiece = self.chessboard.occupiedCases[pieceIndex]
				print("select piece {0}".format(self.currentPiece))


	def draw(self):
		self.getAndDrawGrid()
		if self.pointedSquare != -1:
			self.screen.blit(IMACTIVE_SQUARE,(self.grid[self.pointedSquare][0], self.grid[self.pointedSquare][1]))
		if (self.currentPiece != None):
			for square in self.currentPiece.availableMoves(self.chessboard.occupiedCases):
				if self.currentPiece.isEnemyPiece(self.currentPiece.side, self.chessboard.occupiedCases, square):#add a visual element to let the player know he can capture a piece
					self.screen.blit(IMCAPTURE,(self.grid[square][0], self.grid[square][1]))
				else:
					self.screen.blit(IMVALID,(self.grid[square][0], self.grid[square][1]))#add a visual element to let the player know the available squares

		self.drawPieces()
		pygame.display.flip()

	def drawPieces(self):
		for piece in self.chessboard.occupiedCases:
			if piece.type == EPiece.PAWN:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWP,self.grid[piece.coord])
				else:
					self.screen.blit(IMBP,self.grid[piece.coord])
			if piece.type == EPiece.ROOK:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWR,self.grid[piece.coord])
				else:
					self.screen.blit(IMBR,self.grid[piece.coord])
			if piece.type == EPiece.KNIGHT:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWK,self.grid[piece.coord])
				else:
					self.screen.blit(IMBK,self.grid[piece.coord])
			if piece.type == EPiece.BISHOP:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWB,self.grid[piece.coord])
				else:
					self.screen.blit(IMBB,self.grid[piece.coord])
			if piece.type == EPiece.QUEEN:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWQ,self.grid[piece.coord])
				else:
					self.screen.blit(IMBQ,self.grid[piece.coord])
			if piece.type == EPiece.KING:
				if piece.side == ESide.WHITE:
					self.screen.blit(IMWKING,self.grid[piece.coord])
				else:
					self.screen.blit(IMBKING,self.grid[piece.coord])
	
	def retrieveCoordFromMouseIfAvailable(self):
		case = self.retrieveCoordFromMouse()
		if (self.currentPiece != None):
			return case if case in self.currentPiece.availableMoves(self.chessboard.occupiedCases) or case == self.currentPiece.coord else -1
		else:
			for piece in self.chessboard.occupiedCases:
					if self.turn == ESide.WHITE:                  
						if piece.coord == case and piece.side == ESide.WHITE: return case
					else: 
						if piece.coord == case and piece.side == ESide.BLACK: return case
			return -1

	def retrieveCoordFromMouse(self):
		mouse = pg.mouse.get_pos()
		for index in range (64):
			if ( self.grid[index][0] < mouse[0] < self.grid[index][0] + SQUARE_SIDE ) and ( self.grid[index][1] < mouse[1] < self.grid[index][1] + SQUARE_SIDE):
				return index
		return -1

	def switchTurn(self):
		self.turn = ESide.WHITE if self.turn == ESide.BLACK else ESide.BLACK


	def initDraw(self):
		self.screen.blit(BG_GAME,(0,0))

	def getAndDrawGrid(self):
		squares = []
		debug = 0
		for j in range (8):
			debug = j #allow j to reset after it got scaled to the screen size
			for i in range (8):
				j = debug
				test = False

				if (j+i)%2 == 0:
					i = BORDER + BORDER_TO_CHESSBOARD + (i * SQUARE_SIDE)
					j = BORDER_TO_CHESSBOARD + j * SQUARE_SIDE
					squares.append(self.printSquare( j, i, WHITESQUARE))

				else:
					i = BORDER + BORDER_TO_CHESSBOARD + (i * SQUARE_SIDE)
					j = BORDER_TO_CHESSBOARD + j * SQUARE_SIDE
					squares.append(self.printSquare( j, i, BLACKSQUARE))
		return squares

	def printSquare(self, y, x, square):
		self.screen.blit(square,(x,y))
		return(x,y)
					
g = Game()