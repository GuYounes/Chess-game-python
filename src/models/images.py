import sys
import os
sys.path.append(os.path.join("../../"))
import pygame
from config.settings import SCALE

SCALE100 = int(SCALE * 100)
SCALE200 = int(SCALE * 200)
SCALE1000 = int(SCALE * 1000)
SCALE1500 = int(SCALE * 1500)
#Backgrounds
BG_MENU = pygame.image.load('./../../SetImages1/Background_Menu.png')
BG_GAME = pygame.image.load('./../../SetImages1/Background_Loop.png')
#Icon = pygame.image.load('./../../SetImages1/ico.jpg')

#Menu Buttons
Imboutton_j1i = pygame.image.load('./../../SetImages1/Imboutton_j1i.png')
Imboutton_j1a = pygame.image.load('./../../SetImages1/Imboutton_j1a.png')
Imboutton_j1c = pygame.image.load('./../../SetImages1/Imboutton_j1c.png')

Imboutton_j2i = pygame.image.load('./../../SetImages1/Imboutton_j2i.png')
Imboutton_j2a = pygame.image.load('./../../SetImages1/Imboutton_j2a.png')
Imboutton_j2c = pygame.image.load('./../../SetImages1/Imboutton_j2c.png')

Imboutton_setupi = pygame.image.load('./../../SetImages1/Imboutton_setupi.png')
Imboutton_setupa = pygame.image.load('./../../SetImages1/Imboutton_setupa.png')
Imboutton_setupc = pygame.image.load('./../../SetImages1/Imboutton_setupc.png')

Imboutton_quiti = pygame.image.load('./../../SetImages1/Imboutton_quiti.png')
Imboutton_quita = pygame.image.load('./../../SetImages1/Imboutton_quita.png')
Imboutton_quitc = pygame.image.load('./../../SetImages1/Imboutton_quitc.png')

#Chessboard Buttons
Imboutton_MainMenui = pygame.image.load('./../../SetImages1/Imboutton_MainMenui.png')
Imboutton_MainMenua = pygame.image.load('./../../SetImages1/Imboutton_MainMenua.png')
Imboutton_MainMenuc = pygame.image.load('./../../SetImages1/Imboutton_MainMenuc.png')

Imboutton_NewGamei = pygame.image.load('./../../SetImages1/Imboutton_NewGamei.png') 
Imboutton_NewGamea = pygame.image.load('./../../SetImages1/Imboutton_NewGamea.png')
Imboutton_NewGamec = pygame.image.load('./../../SetImages1/Imboutton_NewGamec.png') 

Imboutton_Undoi = pygame.image.load('./../../SetImages1/Imboutton_Undoi.png')
Imboutton_Undoa = pygame.image.load('./../../SetImages1/Imboutton_Undoa.png')
Imboutton_Undoc = pygame.image.load('./../../SetImages1/Imboutton_Undoc.png')

#Chessboard squares
IMVALID = pygame.image.load('./../../SetImages1/validation.png')
IMCAPTURE = pygame.image.load('./../../SetImages1/elimination.png')
IMACTIVE_SQUARE = pygame.image.load('./../../SetImages1/ACTIVE_SQUARE.png')
WHITESQUARE = pygame.image.load('./../../SetImages1/CaseBlanche.png')
BLACKSQUARE = pygame.image.load('./../../SetImages1/CaseNoire.png')

#Images set1 for pieces
IMWP = pygame.image.load('./../../SetImages1/PIONB.png')
IMBP = pygame.image.load('./../../SetImages1/PIONN.png')
IMWR = pygame.image.load('./../../SetImages1/TOURB.png')
IMBR = pygame.image.load('./../../SetImages1/TOURN.png')
IMWK = pygame.image.load('./../../SetImages1/CAVALIERB.png')
IMBK = pygame.image.load('./../../SetImages1/CAVALIERN.png')
IMWB = pygame.image.load('./../../SetImages1/FOUB.png')
IMBB = pygame.image.load('./../../SetImages1/FOUN.png')
IMWQ = pygame.image.load('./../../SetImages1/DAMEB.png')
IMBQ = pygame.image.load('./../../SetImages1/DAMEN.png')
IMWKING = pygame.image.load('./../../SetImages1/ROIB.png')
IMBKING = pygame.image.load('./../../SetImages1/ROIN.png')

#Images set1 for transformation (could maybe get replaced by a rescale of original images)
MagicalPromotion = pygame.image.load('./../../SetImages1/MagicalPromotion.png')

ImTBi = pygame.image.load('./../../SetImages1/TBi.png')
ImTBa = pygame.image.load('./../../SetImages1/TBa.png')
ImCBi = pygame.image.load('./../../SetImages1/CBi.png')
ImCBa = pygame.image.load('./../../SetImages1/CBa.png')
ImFBi = pygame.image.load('./../../SetImages1/FBi.png')
ImFBa = pygame.image.load('./../../SetImages1/FBa.png')
ImDBi = pygame.image.load('./../../SetImages1/DBi.png')
ImDBa = pygame.image.load('./../../SetImages1/DBa.png')

ImTNi = pygame.image.load('./../../SetImages1/TNi.png')
ImTNa = pygame.image.load('./../../SetImages1/TNa.png')
ImCNi = pygame.image.load('./../../SetImages1/CNi.png')
ImCNa = pygame.image.load('./../../SetImages1/CNa.png')
ImFNi = pygame.image.load('./../../SetImages1/FNi.png')
ImFNa = pygame.image.load('./../../SetImages1/FNa.png')
ImDNi = pygame.image.load('./../../SetImages1/DNi.png')
ImDNa = pygame.image.load('./../../SetImages1/DNa.png')

#Eye animation (for transformation)
oeil_actif = pygame.image.load('./../../Animation oeil/Bouton_Ouvert_hoover.png')

Animation0 = pygame.image.load('./../../Animation oeil/animation_00000.png')
Animation1 = pygame.image.load('./../../Animation oeil/animation_00001.png')
Animation2 = pygame.image.load('./../../Animation oeil/animation_00002.png')
Animation3 = pygame.image.load('./../../Animation oeil/animation_00003.png')
Animation4 = pygame.image.load('./../../Animation oeil/animation_00004.png')
Animation5 = pygame.image.load('./../../Animation oeil/animation_00005.png')
Animation6 = pygame.image.load('./../../Animation oeil/animation_00006.png')
Animation7 = pygame.image.load('./../../Animation oeil/animation_00007.png')
Animation8 = pygame.image.load('./../../Animation oeil/animation_00008.png')
Animation9 = pygame.image.load('./../../Animation oeil/animation_00009.png')
Animation10 = pygame.image.load('./../../Animation oeil/animation_00010.png')
Animation11 = pygame.image.load('./../../Animation oeil/animation_00011.png')
Animation12 = pygame.image.load('./../../Animation oeil/animation_00012.png')
Animation13 = pygame.image.load('./../../Animation oeil/animation_00013.png')
Animation14 = pygame.image.load('./../../Animation oeil/animation_00014.png')
Animation15 = pygame.image.load('./../../Animation oeil/animation_00015.png')
Animation16 = pygame.image.load('./../../Animation oeil/animation_00016.png')
Animation17 = pygame.image.load('./../../Animation oeil/animation_00017.png')
Animation18 = pygame.image.load('./../../Animation oeil/animation_00018.png')
Animation19 = pygame.image.load('./../../Animation oeil/animation_00019.png')
Animation20 = pygame.image.load('./../../Animation oeil/animation_00020.png')
Animation21 = pygame.image.load('./../../Animation oeil/animation_00021.png')
Animation22 = pygame.image.load('./../../Animation oeil/animation_00022.png')
Animation23 = pygame.image.load('./../../Animation oeil/animation_00023.png')
Animation24 = pygame.image.load('./../../Animation oeil/animation_00024.png')
Animation25 = pygame.image.load('./../../Animation oeil/animation_00025.png')
Animation26 = pygame.image.load('./../../Animation oeil/animation_00026.png')
Animation27 = pygame.image.load('./../../Animation oeil/animation_00027.png')
Animation28 = pygame.image.load('./../../Animation oeil/animation_00028.png')
Animation29 = pygame.image.load('./../../Animation oeil/animation_00029.png')
Animation_oeil = [Animation0,Animation1,Animation2,Animation3,Animation4,Animation5,Animation6,Animation7,Animation8,Animation9,Animation10,
				Animation11,Animation12,Animation13,Animation14,Animation15,Animation16,Animation17,Animation18,Animation19,Animation20,
				Animation21,Animation22,Animation23,Animation24,Animation25,Animation26,Animation27,Animation28,Animation29]
			
# RESCALE ------------------------------------------------------------

#Backgrounds
BG_MENU = pygame.transform.scale(BG_MENU,(SCALE1500,SCALE1000))
BG_GAME = pygame.transform.scale(BG_GAME,(SCALE1500,SCALE1000))

#Menu Buttons
Imboutton_j1i = pygame.transform.scale(Imboutton_j1i,(SCALE100,SCALE100))
Imboutton_j1a = pygame.transform.scale(Imboutton_j1a,(SCALE100,SCALE100))
Imboutton_j1c = pygame.transform.scale(Imboutton_j1c,(SCALE100,SCALE100))

Imboutton_j2i = pygame.transform.scale(Imboutton_j2i,(SCALE100,SCALE100))
Imboutton_j2a = pygame.transform.scale(Imboutton_j2a,(SCALE100,SCALE100))
Imboutton_j2c = pygame.transform.scale(Imboutton_j2c,(SCALE100,SCALE100))

Imboutton_setupi = pygame.transform.scale(Imboutton_setupi,(SCALE100,SCALE100))
Imboutton_setupa = pygame.transform.scale(Imboutton_setupa,(SCALE100,SCALE100))
Imboutton_setupc = pygame.transform.scale(Imboutton_setupc,(SCALE100,SCALE100))

Imboutton_quiti = pygame.transform.scale(Imboutton_quiti,(SCALE100,SCALE100))
Imboutton_quita = pygame.transform.scale(Imboutton_quita,(SCALE100,SCALE100))
Imboutton_quitc = pygame.transform.scale(Imboutton_quitc,(SCALE100,SCALE100))

#Chessboard Buttons
Imboutton_MainMenui = pygame.transform.scale(Imboutton_MainMenui,(SCALE100,SCALE100))
Imboutton_MainMenua = pygame.transform.scale(Imboutton_MainMenua,(SCALE100,SCALE100))
Imboutton_MainMenuc = pygame.transform.scale(Imboutton_MainMenuc,(SCALE100,SCALE100))

Imboutton_NewGamei = pygame.transform.scale(Imboutton_NewGamei,(SCALE100,SCALE100)) 
Imboutton_NewGamea = pygame.transform.scale(Imboutton_NewGamea,(SCALE100,SCALE100))
Imboutton_NewGamec = pygame.transform.scale(Imboutton_NewGamec,(SCALE100,SCALE100)) 

Imboutton_Undoi = pygame.transform.scale(Imboutton_Undoi,(SCALE100,SCALE100))
Imboutton_Undoa = pygame.transform.scale(Imboutton_Undoa,(SCALE100,SCALE100))
Imboutton_Undoc = pygame.transform.scale(Imboutton_Undoc,(SCALE100,SCALE100))

#Chessboard squares
IMVALID = pygame.transform.scale(IMVALID,(SCALE100,SCALE100))
IMCAPTURE = pygame.transform.scale(IMCAPTURE,(SCALE100,SCALE100))
IMACTIVE_SQUARE = pygame.transform.scale(IMACTIVE_SQUARE,(SCALE100,SCALE100))
WHITESQUARE = pygame.transform.scale(WHITESQUARE,(SCALE100,SCALE100))
BLACKSQUARE = pygame.transform.scale(BLACKSQUARE,(SCALE100,SCALE100))

#Images set1 for pieces
IMWP = pygame.transform.scale(IMWP,(SCALE100,SCALE100))
IMBP = pygame.transform.scale(IMBP,(SCALE100,SCALE100))
IMWR = pygame.transform.scale(IMWR,(SCALE100,SCALE100))
IMBR = pygame.transform.scale(IMBR,(SCALE100,SCALE100))
IMWK = pygame.transform.scale(IMWK,(SCALE100,SCALE100))
IMBK = pygame.transform.scale(IMBK,(SCALE100,SCALE100))
IMWB = pygame.transform.scale(IMWB,(SCALE100,SCALE100))
IMBB = pygame.transform.scale(IMBB,(SCALE100,SCALE100))
IMWQ = pygame.transform.scale(IMWQ,(SCALE100,SCALE100))
IMBQ = pygame.transform.scale(IMBQ,(SCALE100,SCALE100))
IMWKING = pygame.transform.scale(IMWKING,(SCALE100,SCALE100))
IMBKING = pygame.transform.scale(IMBKING,(SCALE100,SCALE100))

#Images set1 for transformation (could maybe get replaced by a rescale of original images)
MagicalPromotion = pygame.transform.scale(MagicalPromotion,(SCALE100,SCALE100))

ImTBi = pygame.transform.scale(ImTBi,(SCALE200,SCALE200))
ImTBa = pygame.transform.scale(ImTBa,(SCALE200,SCALE200))
ImCBi = pygame.transform.scale(ImCBi,(SCALE200,SCALE200))
ImCBa = pygame.transform.scale(ImCBa,(SCALE200,SCALE200))
ImFBi = pygame.transform.scale(ImFBi,(SCALE200,SCALE200))
ImFBa = pygame.transform.scale(ImFBa,(SCALE200,SCALE200))
ImDBi = pygame.transform.scale(ImDBi,(SCALE200,SCALE200))
ImDBa = pygame.transform.scale(ImDBa,(SCALE200,SCALE200))

ImTNi = pygame.transform.scale(ImTNi,(SCALE200,SCALE200))
ImTNa = pygame.transform.scale(ImTNa,(SCALE200,SCALE200))
ImCNi = pygame.transform.scale(ImCNi,(SCALE200,SCALE200))
ImCNa = pygame.transform.scale(ImCNa,(SCALE200,SCALE200))
ImFNi = pygame.transform.scale(ImFNi,(SCALE200,SCALE200))
ImFNa = pygame.transform.scale(ImFNa,(SCALE200,SCALE200))
ImDNi = pygame.transform.scale(ImDNi,(SCALE200,SCALE200))
ImDNa = pygame.transform.scale(ImDNa,(SCALE200,SCALE200))

#Eye animation (for transformation)
oeil_actif = pygame.transform.scale(oeil_actif,(SCALE100,SCALE100))

Animation0 = pygame.transform.scale(Animation0,(SCALE100,SCALE100))
Animation1 = pygame.transform.scale(Animation1,(SCALE100,SCALE100))
Animation2 = pygame.transform.scale(Animation2,(SCALE100,SCALE100))
Animation3 = pygame.transform.scale(Animation3,(SCALE100,SCALE100))
Animation4 = pygame.transform.scale(Animation4,(SCALE100,SCALE100))
Animation5 = pygame.transform.scale(Animation5,(SCALE100,SCALE100))
Animation6 = pygame.transform.scale(Animation6,(SCALE100,SCALE100))
Animation7 = pygame.transform.scale(Animation7,(SCALE100,SCALE100))
Animation8 = pygame.transform.scale(Animation8,(SCALE100,SCALE100))
Animation9 = pygame.transform.scale(Animation9,(SCALE100,SCALE100))
Animation10 = pygame.transform.scale(Animation10,(SCALE100,SCALE100))
Animation11 = pygame.transform.scale(Animation11,(SCALE100,SCALE100))
Animation12 = pygame.transform.scale(Animation12,(SCALE100,SCALE100))
Animation13 = pygame.transform.scale(Animation13,(SCALE100,SCALE100))
Animation14 = pygame.transform.scale(Animation14,(SCALE100,SCALE100))
Animation15 = pygame.transform.scale(Animation15,(SCALE100,SCALE100))
Animation16 = pygame.transform.scale(Animation16,(SCALE100,SCALE100))
Animation17 = pygame.transform.scale(Animation17,(SCALE100,SCALE100))
Animation18 = pygame.transform.scale(Animation18,(SCALE100,SCALE100))
Animation19 = pygame.transform.scale(Animation19,(SCALE100,SCALE100))
Animation20 = pygame.transform.scale(Animation20,(SCALE100,SCALE100))
Animation21 = pygame.transform.scale(Animation21,(SCALE100,SCALE100))
Animation22 = pygame.transform.scale(Animation22,(SCALE100,SCALE100))
Animation23 = pygame.transform.scale(Animation23,(SCALE100,SCALE100))
Animation24 = pygame.transform.scale(Animation24,(SCALE100,SCALE100))
Animation25 = pygame.transform.scale(Animation25,(SCALE100,SCALE100))
Animation26 = pygame.transform.scale(Animation26,(SCALE100,SCALE100))
Animation27 = pygame.transform.scale(Animation27,(SCALE100,SCALE100))
Animation28 = pygame.transform.scale(Animation28,(SCALE100,SCALE100))
Animation29 = pygame.transform.scale(Animation29,(SCALE100,SCALE100))
Animation_oeil = [Animation0,Animation1,Animation2,Animation3,Animation4,Animation5,Animation6,Animation7,Animation8,Animation9,Animation10,
				Animation11,Animation12,Animation13,Animation14,Animation15,Animation16,Animation17,Animation18,Animation19,Animation20,
				Animation21,Animation22,Animation23,Animation24,Animation25,Animation26,Animation27,Animation28,Animation29]
