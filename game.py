import pygame as pg
from chessboard import ChessBoard, ESide
from piece import Piece
from images import * 
from settings import *

class Game:
	def __init__(self):
		pg.init()
		self.screen = pg.display.set_mode((WIDTHDISPLAY, HEIGHTDISPLAY))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.turn = ESide.WHITE #True for white, False for black
		self.currentPiece = None
		self.new()

	def new(self):
		self.initDraw()
		self.grid = self.getAndPrintGrid() #The key to transit between coords and the screen
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
		self.getAndPrintGrid()
		if self.pointedSquare != -1:
			pygame.draw.rect(self.screen, BRIGHT_GREEN, (self.grid[self.pointedSquare][0], self.grid[self.pointedSquare][1], SQUARE_SIDE, SQUARE_SIDE))
		if (self.currentPiece != None):
			pass
		pygame.display.flip()

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

	def getAndPrintGrid(self):
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