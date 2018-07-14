import pygame as pg
from images import * 
from settings import *

class Main:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTHDISPLAY, HEIGHTDISPLAY))
		pg.display.set_caption(TITLE)
		self.clock = pg.time.Clock()