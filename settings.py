HEIGHTDISPLAY = int(1000)
WIDTHDISPLAY = int((3/2) * HEIGHTDISPLAY)

TITLE = "Chess"
FPS = 60

BORDER = ( 1/3 * WIDTHDISPLAY ) / 2

BORDER_TO_CHESSBOARD = ( HEIGHTDISPLAY * 0.1 )

CHESSBOARD_SIDE = HEIGHTDISPLAY - 2 * BORDER_TO_CHESSBOARD

SQUARE_SIDE = CHESSBOARD_SIDE /8

bouttonmenu_height = int((HEIGHTDISPLAY * 0.7) * (3/20))
bouttonmenu_width = int(HEIGHTDISPLAY * (2/5))
bouttonmenu_heightgap = int((HEIGHTDISPLAY * 0.7 - 4 * bouttonmenu_height) / 5)
bouttonmenu_widthgap = int(WIDTHDISPLAY - bouttonmenu_width) / 2

BRIGHT_BLUE = (20,170,220)
BRIGHT_GREEN = (0,200,0)
'''
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (60,60,60)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BROWN = (110,50,15)
DARK_BROWN = (235,220,192)
'''