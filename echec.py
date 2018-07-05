import pygame
import time

#Les images des pièces doîvent être de case_side x cas_side et les images 
#pour la transformation doivent être deux fois plus grande


pygame.init()

display_height = int(1000)
display_width = int((3/2) * display_height)
border = ( 1/3 * display_width ) / 2
side_gap = ( display_height * 0.1 )
echiquier_side = display_height - 2 * side_gap
case_side = echiquier_side /8
line_width = 10
bouttonmenu_height = int((display_height * 0.7) * (3/20))
bouttonmenu_width = int(display_height * (2/5))
bouttonmenu_heightgap = int((display_height * 0.7 - 4 * bouttonmenu_height) / 5)
bouttonmenu_widthgap = int(display_width - bouttonmenu_width) / 2

B = (60,60,60)
W = (255,255,255)
Dark_B = (0,0,0)
grey = (20,170,220)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
bright_green = (0,200,0)


background = pygame.image.load('Images/fond.jpg')
Icon = pygame.image.load('Images/ico.jpg')
ImbouttonJ1i = pygame.image.load('Images/Image_boutton_menu_inactif.png')
ImbouttonJ1a = pygame.image.load('Images/Image_boutton_menu_actif.png')
Imvalidation = pygame.image.load('Images/validation.png')
Imelimination = pygame.image.load('Images/elimination.png')
Impb = pygame.image.load('Images/PIONB.png')
Impn = pygame.image.load('Images/PIONN.png')
Imtb = pygame.image.load('Images/TOURB.png')
Imtn = pygame.image.load('Images/TOURN.png')
Imcb = pygame.image.load('Images/CAVALIERB.png')
Imcn = pygame.image.load('Images/CAVALIERN.png')
Imfb = pygame.image.load('Images/FOUB.png')
Imfn = pygame.image.load('Images/FOUN.png')
Imdb = pygame.image.load('Images/DAMEB.png')
Imdn = pygame.image.load('Images/DAMEN.png')
Imrb = pygame.image.load('Images/ROIB.png')
Imrn = pygame.image.load('Images/ROIN.png')

#pour la fonction transformation
Im_showi = pygame.image.load('Images/Im_showi.png')
Im_showa = pygame.image.load('Images/Im_showa.png')

ImTBi = pygame.image.load('Images/TBi.png')
ImTBa = pygame.image.load('Images/TBa.png')
ImCBi = pygame.image.load('Images/CBi.png')
ImCBa = pygame.image.load('Images/CBa.png')
ImFBi = pygame.image.load('Images/FBi.png')
ImFBa = pygame.image.load('Images/FBa.png')
ImDBi = pygame.image.load('Images/DBi.png')
ImDBa = pygame.image.load('Images/DBa.png')

ImagesImTNi = pygame.image.load('Images/TNi.png')
ImagesImTNa = pygame.image.load('Images/TNa.png')
ImagesImCNi = pygame.image.load('Images/CNi.png')
ImagesImCNa = pygame.image.load('Images/CNa.png')
ImagesImFNi = pygame.image.load('Images/FNi.png')
ImagesImFNa = pygame.image.load('Images/FNa.png')
ImagesImDNi = pygame.image.load('Images/DNi.png')
ImDNa = pygame.image.load('Images/DNa.png')


gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(Dark_B)
pygame.display.set_caption('C\'est l\'heure du DUDUDUEL')
pygame.display.set_icon(Icon)
clock = pygame.time.Clock()


tab120 = (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1,  0,  1,  2,  3,  4,  5,  6,  7, -1,
		-1,  8,  9, 10, 11, 12, 13, 14, 15, -1,
		-1, 16, 17, 18, 19, 20, 21, 22, 23, -1,
		-1, 24, 25, 26, 27, 28, 29, 30, 31, -1,
		-1, 32, 33, 34, 35, 36, 37, 38, 39, -1,
		-1, 40, 41, 42, 43, 44, 45, 46, 47, -1,
		-1, 48, 49, 50, 51, 52, 53, 54, 55, -1,
		-1, 56, 57, 58, 59, 60, 61, 62, 63, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
		-1, -1, -1, -1, -1, -1, -1, -1, -1, -1)

tab64 = (21, 22, 23, 24, 25, 26, 27, 28,
		31, 32, 33, 34, 35, 36, 37, 38,
		41, 42, 43, 44, 45, 46, 47, 48,
		51, 52, 53, 54, 55, 56, 57, 58,
		61, 62, 63, 64, 65, 66, 67, 68,
		71, 72, 73, 74, 75, 76, 77, 78,
		81, 82, 83, 84, 85, 86, 87, 88,
		91, 92, 93, 94, 95, 96, 97, 98)


        
class vide:
	equipe = "neutre"
	rang = "vide"
	valeur = 0
	def __init__(self):
		pass

class white:

	def __init__(self):
		self.equipe = "blanc"
		self.isselected = False

	def select(cls, piece, liste_plateau, liste_case):
		pygame.display.update()
		liste_deplacement = piece.voir_deplacement(piece, liste_plateau, liste_case)
		piece.isselected = True
		while piece.isselected:

			for event in pygame.event.get():
				mouse = pygame.mouse.get_pos()
				click = pygame.mouse.get_pressed()

				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				for j in liste_deplacement:
					if liste_plateau[j].equipe == "neutre":
						gameDisplay.blit(Imvalidation,(liste_case[j][0], liste_case[j][1]))
					else:
						gameDisplay.blit(Imelimination,(liste_case[j][0], liste_case[j][1]))
					printpieces(liste_plateau,liste_case)
					pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					for i in liste_deplacement:
						if (liste_case[i][0] < mouse[0] < liste_case[i][0] + case_side) and (liste_case[i][1] < mouse[1] < liste_case[i][1] + case_side):
							liste_plateau = piece.deplacement(liste_plateau, piece, i, liste_case)
					piece.isselected = False
		return liste_plateau

					

	def voir_deplacement(self, piece, liste_plateau, liste_case):

		liste_deplacement = []
		indice_piece = liste_plateau.index(piece)
		valeur_64 = tab64[indice_piece]

		if piece.rang == "cavalier":
			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe != "blanc":
						liste_deplacement.append(valeur120)

		elif piece.rang == "tour" or piece.rang == "fou" or piece.rang == "dame":
			for i in piece.valeur_deplacement:
				for j in range (1,7):
					try:
						valeur120 = tab120[valeur_64 + i *j ]

						if valeur120 != -1:
							if liste_plateau[valeur120].equipe != "blanc":
								liste_deplacement.append(valeur120)
								if liste_plateau[valeur120].equipe == "noir":
									break

							elif liste_plateau[valeur120].equipe == "blanc"	:
								break
												
						elif valeur120 == -1:
							break
					except:
						break
					finally:
						pass

		elif piece.rang == "pion":
			if not piece.moved:
				if liste_plateau[ indice_piece - 8 ].equipe == "neutre":
					piece.valeur_deplacement = [ -10, -20 ]
				else:
					piece.valeur_deplacement = [ -10 ]

			elif piece.moved:
				piece.valeur_deplacement = [ -10 ]

			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i ]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe == "neutre":
						liste_deplacement.append(valeur120)

			if liste_plateau[indice_piece - 9].equipe == "noir" and tab120[ valeur_64 - 11 ] != -1:
				liste_deplacement.append( tab120[ valeur_64 - 11 ]) 
			if liste_plateau[indice_piece - 7].equipe == "noir" and tab120[ valeur_64 - 9 ] != -1:
				liste_deplacement.append( tab120[ valeur_64 - 9 ])

		elif piece.rang == "roi":
			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe != "blanc":
						liste_deplacement.append(valeur120)
			if not piece.moved and not tb1.moved and liste_plateau[57].equipe == "neutre" and liste_plateau[58].equipe == "neutre" and liste_plateau[59].equipe == "neutre" and not piece.echec:
				liste_deplacement.append(58)
			if not piece.moved and not tb2.moved and liste_plateau[61].equipe == "neutre" and liste_plateau[62].equipe == "neutre" and not piece.echec:
				liste_deplacement.append(62)

		return liste_deplacement
	
		
	def deplacement(cls, liste_plateau, piece, i, liste_case):

		indice_piece = liste_plateau.index(piece)

		grandrock = (piece.rang == "roi") and i == 58

		petitrock = (piece.rang == "roi") and i == 62

		if piece.rang == "pion" or piece.rang == "tour" or piece.rang == "roi":
			piece.moved = True

		if grandrock:
			liste_plateau[indice_piece], liste_plateau[i] = liste_plateau[i], liste_plateau[indice_piece]
			liste_plateau[56], liste_plateau[59] = liste_plateau[59], liste_plateau[56]
			return liste_plateau

		if petitrock:
			liste_plateau[indice_piece], liste_plateau[i] = liste_plateau[i], liste_plateau[indice_piece]
			liste_plateau[63], liste_plateau[61] = liste_plateau[61], liste_plateau[63]
			return liste_plateau

		if liste_plateau[i].equipe == "neutre" and not grandrock and not petitrock:
			liste_plateau[i], liste_plateau[indice_piece] = liste_plateau[indice_piece], liste_plateau[i]
			if piece.rang == "pion" and 8 <= indice_piece <=15:
				echiquier()
				printpieces(liste_plateau, liste_case)
				transformation("blanc", piece, liste_plateau, liste_case)
			return liste_plateau

		else:
			liste_plateau[i].equipe,liste_plateau[i].rang = "neutre", "vide"
			liste_plateau[i], liste_plateau[indice_piece] = liste_plateau[indice_piece], liste_plateau[i]
			if piece.rang == "pion" and 8 <= indice_piece <=15:
				echiquier()
				printpieces(liste_plateau, liste_case)
				transformation("blanc", piece, liste_plateau, liste_case)
			return liste_plateau


class wpion(white):
	rang = "pion"
	valeur = 1
	valeur_deplacement = ["whatever"]
	moved = False

	def __init__(self):
		white.__init__(self)

class wtour(white):
	rang = "tour"
	valeur = 5
	valeur_deplacement = [ -10, +10, -1, +1 ]
	moved = False

	def __init__(self):
		white.__init__(self)


class wcavalier(white):
	rang = "cavalier"
	valeur = 3
	valeur_deplacement = [ -12,-21, -19, -8, 12, 21, 19, 8 ]

	def __init__(self):
		white.__init__(self)

class wfou(white):
	rang = "fou"
	valeur = 3
	valeur_deplacement = [ -11, -9, +11, +9 ]

	def __init__(self):
		white.__init__(self)

class wdame(white):
	rang = "dame"
	valeur = 10
	valeur_deplacement = [ -10, +10, -1, +1, -11, -9, +11, +9 ]

	def __init__(self):
		white.__init__(self)

class wroi(white):
	rang = "roi"
	valeur = 100
	valeur_deplacement = [ -10, +10, -1, +1, -11, -9, +11, +9 ]
	echec = False
	moved = False

	def __init__(self):
		white.__init__(self)


class black:

	def __init__(self):
		self.equipe = "noir"
		self.isselected = False

	def select(cls, piece, liste_plateau, liste_case):
		pygame.display.update()
		liste_deplacement = piece.voir_deplacement(piece, liste_plateau, liste_case)
		piece.isselected = True
		while piece.isselected:

			for event in pygame.event.get():
				mouse = pygame.mouse.get_pos()
				click = pygame.mouse.get_pressed()

				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				for j in liste_deplacement:
					if liste_plateau[j].equipe == "neutre":
						gameDisplay.blit(Imvalidation,(liste_case[j][0], liste_case[j][1]))
					else:
						gameDisplay.blit(Imelimination,(liste_case[j][0], liste_case[j][1]))
					printpieces(liste_plateau,liste_case)
					pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					for i in liste_deplacement:
						if (liste_case[i][0] < mouse[0] < liste_case[i][0] + case_side) and (liste_case[i][1] < mouse[1] < liste_case[i][1] + case_side):
							liste_plateau = piece.deplacement(liste_plateau, piece, i, liste_case)
					piece.isselected = False

		return liste_plateau

	def voir_deplacement(self, piece, liste_plateau, liste_case):

		liste_deplacement = []
		indice_piece = liste_plateau.index(piece)
		valeur_64 = tab64[indice_piece]

		if piece.rang == "cavalier":
			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe != "noir":
						liste_deplacement.append(valeur120)

		elif piece.rang == "tour" or piece.rang == "fou" or piece.rang == "dame":
			for i in piece.valeur_deplacement:
				for j in range (1,7):
					try:
						valeur120 = tab120[valeur_64 + i *j ]

						if valeur120 != -1:
							if liste_plateau[valeur120].equipe != "noir":
								liste_deplacement.append(valeur120)
								if liste_plateau[valeur120].equipe == "blanc":
									break

							elif liste_plateau[valeur120].equipe == "noir"	:
								break
												
						elif valeur120 == -1:
							break
					except:
						break
					finally:
						pass


		elif piece.rang == "pion":
			if not piece.moved:
				if liste_plateau[ indice_piece + 8 ].equipe == "neutre":
					piece.valeur_deplacement = [ +10, +20 ]
				else:
					piece.valeur_deplacement = [ +10 ]

			elif piece.moved:
				piece.valeur_deplacement = [ +10 ]

			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i ]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe == "neutre":
						liste_deplacement.append(valeur120)

						
			if indice_piece + 9 <= 63:			
				if liste_plateau[indice_piece + 9].equipe == "blanc" and tab120[ valeur_64 + 11 ] != -1:
					liste_deplacement.append( tab120[ valeur_64 + 11 ])

			if liste_plateau[indice_piece + 7].equipe == "blanc" and tab120[ valeur_64 + 9 ] != -1:
					liste_deplacement.append( tab120[ valeur_64 + 9 ])
				
		elif piece.rang == "roi":
			for i in piece.valeur_deplacement:
				valeur120 = tab120[valeur_64 + i]
				if valeur120 != -1:
					if liste_plateau[valeur120].equipe != "noir":
						liste_deplacement.append(valeur120)
				if not piece.moved and not tn1.moved and liste_plateau[1].equipe == "neutre" and liste_plateau[2].equipe == "neutre" and liste_plateau[3].equipe == "neutre" and not piece.echec:
					liste_deplacement.append(2)
				if not piece.moved and not tn2.moved and liste_plateau[5].equipe == "neutre" and liste_plateau[6].equipe == "neutre" and not piece.echec:
					liste_deplacement.append(6)

					

		return liste_deplacement
	
		
	def deplacement(cls, liste_plateau, piece, i, liste_case):

		indice_piece = liste_plateau.index(piece)

		grandrock = (piece.rang == "roi") and i == 2

		petitrock = (piece.rang == "roi") and i == 6

		if piece.rang == "pion" or piece.rang == "tour" or piece.rang == "roi":
			piece.moved = True


		if grandrock:
			liste_plateau[indice_piece], liste_plateau[i] = liste_plateau[i], liste_plateau[indice_piece]
			liste_plateau[0], liste_plateau[3] = liste_plateau[3], liste_plateau[0]
			return liste_plateau

		if petitrock:
			liste_plateau[indice_piece], liste_plateau[i] = liste_plateau[i], liste_plateau[indice_piece]
			liste_plateau[7], liste_plateau[5] = liste_plateau[5], liste_plateau[7]
			print("petit")
			return liste_plateau

		if liste_plateau[i].equipe == "neutre" and not petitrock and not grandrock:
			liste_plateau[i], liste_plateau[indice_piece] = liste_plateau[indice_piece], liste_plateau[i]
			if piece.rang == "pion" and 48 <= indice_piece <= 55:
				echiquier()
				printpieces(liste_plateau, liste_case)
				transformation("noir",piece, liste_plateau, liste_case)
			return liste_plateau

		else:
			liste_plateau[i].equipe,liste_plateau[i].rang = "neutre", "vide"
			liste_plateau[i], liste_plateau[indice_piece] = liste_plateau[indice_piece], liste_plateau[i]
			if piece.rang == "pion" and 48 <= indice_piece <= 55:
				echiquier()
				printpieces(liste_plateau, liste_case)
				transformation("noir", piece, liste_plateau, liste_case)
			return liste_plateau



class bpion(black):
	rang = "pion"
	valeur = 1
	valeur_deplacement = ["whatever"]
	moved = False

	def __init__(self):
		black.__init__(self)

class btour(black):
	rang = "tour"
	valeur = 5
	valeur_deplacement = [ -10, +10, -1, +1 ]
	moved = False

	def __init__(self):
		black.__init__(self)


class bcavalier(black):
	rang = "cavalier"
	valeur = 3
	valeur_deplacement = [ -12,-21, -19, -8, 12, 21, 19, 8 ]

	def __init__(self):
		black.__init__(self)

class bfou(black):
	rang = "fou"
	valeur = 3
	valeur_deplacement = [ -11, -9, +11, +9 ]

	def __init__(self):
		black.__init__(self)

class bdame(black):
	rang = "dame"
	valeur = 10
	valeur_deplacement = [ -10, +10, -1, +1, -11, -9, +11, +9 ]

	def __init__(self):
		black.__init__(self)

class broi(black):
	rang = "roi"
	valeur = 100
	valeur_deplacement = [ -10, +10, -1, +1, -11, -9, +11, +9 ]
	echec = False
	moved = False

	def __init__(self):
		black.__init__(self)

pb1 = wpion()
pb2 = wpion()
pb3 = wpion()
pb4 = wpion()
pb5 = wpion()
pb6 = wpion()
pb7 = wpion()
pb8 = wpion()

pn1 = bpion()
pn2 = bpion()
pn3 = bpion()
pn4 = bpion()
pn5 = bpion()
pn6 = bpion()
pn7 = bpion()
pn8 = bpion()

tb1 = wtour()
tb2 = wtour()

tn1 = btour()
tn2 = btour()

cb1 = wcavalier()
cb2 = wcavalier()

cn1 = bcavalier()
cn2 = bcavalier()

fb1 = wfou()
fb2 = wfou()

fn1 = bfou()
fn2 = bfou()

db = wdame()

dn = bdame()

rb = wroi()

rn = broi()


def button( x, y, Imagei, Imagea, fonction, image_width, image_height,*args ):
	gameDisplay.blit(Imagei,(x, y))
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if len(args) == 2 :
		a = args[0]
		b = args[1]
	if x < mouse[0] < x + image_width and y < mouse[1] < y + image_height:
		gameDisplay.blit(Imagea,(x, y))
		if click[0] == 1:
			gameDisplay.blit(Imagea,(x, y))
			if len(args) == 2 :
				fonction(a,b)
			else:
				fonction()
	pygame.display.update()

def button_noclick( x, y, Imagei, Imagea, fonction, image_width, image_height,*args ):
	gameDisplay.blit(Imagei,(x, y))
	mouse = pygame.mouse.get_pos()
	if len(args) == 2 :
		a = args[0]
		b = args[1]
	if x < mouse[0] < x + image_width and y < mouse[1] < y + image_height:
		gameDisplay.blit(Imagea,(x, y))
		if len(args) == 2 :
			fonction(a,b)
		else:
			fonction()
	pygame.display.update()


def placement_pieces():

	liste_vi=[]

	for j in range (32):
		vi = vide()
		liste_vi.append(vi)

	echiquier=[tn1, cn1, fn1, dn, rn, fn2, cn2, tn2, pn1, pn2, pn3, pn4, pn5,pn6, pn7, pn8] 
	echiquier.extend(liste_vi)
	echiquier.extend([pb1, pb2, pb3, pb4, pb5, pb6, pb7, pb8, tb1, cb1, fb1, db, rb, fb2, cb2, tb2])

	return echiquier


def print_echiquiercase(y, x, ic):
	pygame.draw.rect(gameDisplay , ic, (x, y, case_side, case_side))
	return(x,y)


def echiquier():
	
	list_definecase = []
	debug = 0
	for j in range (8):
		debug = j
		for i in range (8):
			j = debug
			test = False

			if (j+i)%2 == 0:
				i = border + side_gap + (i * case_side)
				j = side_gap + j * case_side
				list_definecase.append(print_echiquiercase( j, i, W))

			else:
				i = border + side_gap + (i * case_side)
				j = side_gap + j * case_side
				list_definecase.append(print_echiquiercase( j, i, B))
	return list_definecase



def buttons_plateau( White, liste_case, liste_plateau ):
	echiquier()
	mouse = pygame.mouse.get_pos()
	for i in range (64):
		if ( liste_case[i][0] < mouse[0] < liste_case[i][0] + case_side ) and ( liste_case[i][1] < mouse[1] < liste_case[i][1] + case_side):
			if liste_plateau[i].equipe != "neutre":
				if ( White and liste_plateau[i].equipe == "blanc" ) or ( not White and liste_plateau[i].equipe == "noir" ):				
					pygame.draw.rect(gameDisplay, grey, (liste_case[i][0], liste_case[i][1], case_side, case_side))
	printpieces(liste_plateau,liste_case)
	pygame.display.update()

def tf(rang, piece):
	piece.rang = rang
	if rang == "tour":
		piece.valeur_deplacement = [ +1, -1, +10, -10]
	elif rang == "cavalier":
		piece.valeur_deplacement = [ -12,-21, -19, -8, 12, 21, 19, 8 ]
	elif rang == "fou":
		piece.valeur_deplacement = [ -11, -9, +11, +9 ]
	else:
		piece.valeur_deplacement = [ -10, +10, -1, +1, -11, -9, +11, +9 ]


def transformation(equipe, piece, liste_plateau, liste_case):
	printpieces(liste_plateau,liste_case)
	pygame.draw.rect(gameDisplay , Dark_B, (border, display_height/2 - (3/2) * case_side, echiquier_side + 2 * side_gap, case_side * 3))
	pygame.display.update()
	boucle_transformation = True
	while boucle_transformation:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		if equipe == "blanc":
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 1 + (2 * case_side) * 0 + border, display_height/2 - case_side, ImTBi, ImTBa,tf , case_side * 2, case_side * 2, "tour", piece)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 2 + (2 * case_side) * 1 + border, display_height/2 - case_side, ImCBi, ImCBa,tf , case_side * 2, case_side * 2, "cavalier", piece)
			button_noclick( border + echiquier_side + 2 * side_gap + 0.15 * border, 0.15 * border, Im_showi, Im_showa, refresh_transformation, border * 0.7, border*0.7, liste_plateau, liste_case)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 3 + (2 * case_side) * 2 + border, display_height/2 - case_side, ImFBi, ImFBa,tf , case_side * 2, case_side * 2, "fou", piece)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 4 + (2 * case_side) * 3 + border, display_height/2 - case_side, ImDBi, ImDBa,tf , case_side * 2, case_side * 2, "dame", piece)
		
		elif equipe == "noir":
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 1 + (2 * case_side) * 0 + border, display_height/2 - case_side, ImTNi, ImTNa,tf , case_side * 2, case_side * 2, "tour", piece)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 2 + (2 * case_side) * 1 + border, display_height/2 - case_side, ImCNi, ImCNa,tf , case_side * 2, case_side * 2, "cavalier", piece)
			button_noclick( border + echiquier_side + 2 * side_gap + 0.15 * border, 0.15 * border, Im_showi, Im_showa, refresh_transformation, border * 0.7, border*0.7, liste_plateau, liste_case)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 3 + (2 * case_side) * 2 + border, display_height/2 - case_side, ImFNi, ImFNa,tf , case_side * 2, case_side * 2, "fou", piece)
			button((((display_width - 2 * border) - 4 * 2 * case_side)/5) * 4 + (2 * case_side) * 3 + border, display_height/2 - case_side, ImDNi, ImDNa,tf , case_side * 2, case_side * 2, "dame", piece)
		
		if piece.rang != "pion":
			boucle_transformation = False

	gameDisplay.blit(background,(border,0))
	echiquier()
	printpieces(liste_plateau,liste_case)
	pygame.display.update()
	




def white_plays( liste_case, liste_plateau ):
	mouse = pygame.mouse.get_pos()
	save = list(liste_plateau)
	click = pygame.mouse.get_pressed()
	for i in range (64):
		if ( liste_case[i][0] < mouse[0] < liste_case[i][0] + case_side ) and ( liste_case[i][1] < mouse[1] < liste_case[i][1] + case_side):
			if liste_plateau[i].equipe == "blanc":
				if click[0] == 1:
					liste_plateau = liste_plateau[i].select(liste_plateau[i], liste_plateau, liste_case)
	if liste_plateau == save:
		return True
	else:
		return False

def black_plays( liste_case, liste_plateau ):
	mouse = pygame.mouse.get_pos()
	save = list(liste_plateau)
	click = pygame.mouse.get_pressed()
	for i in range (64):
		if ( liste_case[i][0] < mouse[0] < liste_case[i][0] + case_side ) and ( liste_case[i][1] < mouse[1] < liste_case[i][1] + case_side):
			if liste_plateau[i].equipe == "noir":
				if click[0] == 1:
					liste_plateau = liste_plateau[i].select(liste_plateau[i], liste_plateau, liste_case)
	if liste_plateau == save:
		return False
	else:
		return True

def play( White, liste_case, liste_plateau ):
	buttons_plateau( White, liste_case, liste_plateau)
	if White:
		White = white_plays( liste_case, liste_plateau)
	else:
		White = black_plays( liste_case, liste_plateau)

	return White, liste_plateau

def printpieces(liste_plateau,liste_case):
	for i in range (64):
		if liste_plateau[i].rang == "pion":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Impb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Impn,(liste_case[i]))

		if liste_plateau[i].rang == "tour":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Imtb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Imtn,(liste_case[i]))

		if liste_plateau[i].rang == "cavalier":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Imcb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Imcn,(liste_case[i]))

		if liste_plateau[i].rang == "fou":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Imfb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Imfn,(liste_case[i]))

		if liste_plateau[i].rang == "dame":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Imdb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Imdn,(liste_case[i]))

		if liste_plateau[i].rang == "roi":
			if liste_plateau[i].equipe == "blanc":
				gameDisplay.blit(Imrb,(liste_case[i]))
			elif liste_plateau[i].equipe == "noir":
				gameDisplay.blit(Imrn,(liste_case[i]))

def refresh_false():
	mouse = pygame.mouse.get_pos()
	if border + echiquier_side + 2 * side_gap + border * 0.15 < mouse[0] < border + echiquier_side + 2 * side_gap + border * 0.15 + border * 0.7 and border * 0.15 < mouse[1] < border * 0.15 + border * 0.7:
		return True
	else:
		return False


def refresh_transformation(liste_plateau, liste_case):
	gameDisplay.blit(background,(border,0))
	echiquier()
	printpieces(liste_plateau, liste_case)
	pygame.display.update()
	boucle_refresh = True
	while boucle_refresh:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		boucle_refresh = refresh_false()
		pygame.display.update()

	gameDisplay.blit(background,(border,0))
	echiquier()
	printpieces(liste_plateau, liste_case)
	pygame.draw.rect(gameDisplay , Dark_B, (border, display_height/2 - (3/2) * case_side, echiquier_side + 2 * side_gap, case_side * 3))
	pygame.display.update()


def game_loop():

	gameDisplay.blit(background,(border,0))

	liste_plateau = placement_pieces()

	liste_case = echiquier() 

	printpieces(liste_plateau,liste_case)

	pygame.display.update()

	King = True
	White = True
	
	while King:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			White, liste_plateau = play( White, liste_case, liste_plateau)
			pygame.display.update()
		clock.tick(120)

def game_menu():

	intro = True
	gameDisplay.fill(B)
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		button( bouttonmenu_widthgap, bouttonmenu_heightgap * 1 + 0.3 * display_height + bouttonmenu_height * 0, ImbouttonJ1i, ImbouttonJ1a, game_loop, bouttonmenu_width, bouttonmenu_height )
		button( bouttonmenu_widthgap, bouttonmenu_heightgap * 2 + 0.3 * display_height + bouttonmenu_height * 1 , ImbouttonJ1i, ImbouttonJ1a, game_loop, bouttonmenu_width, bouttonmenu_height )
		button( bouttonmenu_widthgap, bouttonmenu_heightgap * 3 + 0.3 * display_height + bouttonmenu_height * 2, ImbouttonJ1i, ImbouttonJ1a, game_loop, bouttonmenu_width, bouttonmenu_height )
		button( bouttonmenu_widthgap, bouttonmenu_heightgap * 4 + 0.3 * display_height + bouttonmenu_height * 3, ImbouttonJ1i, ImbouttonJ1a, game_loop, bouttonmenu_width, bouttonmenu_height )
		pygame.display.update()
		clock.tick(120)




game_menu()
pygame.quit()
quit()
