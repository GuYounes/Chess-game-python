import pygame as pg
from chessboard import *
from piece import Piece
from images import * 
from settings import *

class Game:
	def __init__(self):
		pygame.init()
		self.screen = pg.display.set_mode((WIDTHDISPLAY, HEIGHTDISPLAY))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()
		self.turn = True #True for white, False for black
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
		for event in pg.event.get():

			click = pg.mouse.get_pressed()

			if event.type == pg.QUIT:
				pg.quit()
				quit()
		
			self.pointedSquare = self.updateMouse()
			self.pointedSquareIsActiv = False
			for piece in self.chessboard.occupiedCases:#  not necessary but helps
				if piece.coord == self.pointedSquare:#    to understand the path taken
					if self.turn:                  
						for piece in self.chessboard.playerWhite.pieces:
							if piece.coord == self.pointedSquare: self.pointedSquareIsActiv = True
					else: 
						for piece in self.chessboard.playerBlack.pieces:
							if piece.coord == self.pointedSquare: self.pointedSquareIsActiv = True
			
			if self.pointedSquareIsActiv and click[0] == 1:
				self.selectPiece()
			

	def draw(self):
		self.getAndPrintGrid()
		if self.pointedSquareIsActiv:
			pg.draw.rect(self.screen, BRIGHT_GREEN, (self.grid[self.pointedSquare][0], self.grid[self.pointedSquare][1], SQUARE_SIDE, SQUARE_SIDE))
		pygame.display.flip()

	def updateMouse(self):
		mouse = pg.mouse.get_pos()
		for index in range (64):
			if ( self.grid[index][0] < mouse[0] < self.grid[index][0] + SQUARE_SIDE ) and ( self.grid[index][1] < mouse[1] < self.grid[index][1] + SQUARE_SIDE):
				return index


	def initDraw(self):
		self.screen.blit(BG_GAME,(0,0))

	def getAndPrintGrid(self):
		list_defineSquare = []
		debug = 0
		for j in range (8):
			debug = j #allow j to reset after it got scaled to the screen size
			for i in range (8):
				j = debug
				test = False

				if (j+i)%2 == 0:
					i = BORDER + BORDER_TO_CHESSBOARD + (i * SQUARE_SIDE)
					j = BORDER_TO_CHESSBOARD + j * SQUARE_SIDE
					list_defineSquare.append(self.printSquare( j, i, WHITESQUARE))

				else:
					i = BORDER + BORDER_TO_CHESSBOARD + (i * SQUARE_SIDE)
					j = BORDER_TO_CHESSBOARD + j * SQUARE_SIDE
					list_defineSquare.append(self.printSquare( j, i, BLACKSQUARE))
		return list_defineSquare

	def printSquare(self, y, x, square ):
		self.screen.blit(square,(x,y))
		return(x,y)

	def selectPiece(self):
		self.PieceIsSelected = True
		while self.PieceIsSelected:
			for move in self.chessboard.playerWhite.availableMoves(self.occupiedCases):
				print("ça marche")
		


g = Game()