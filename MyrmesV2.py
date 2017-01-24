import time
date = time.strftime('%d/%m/%y à %H:%M',time.localtime())

import os
colors = {'grey': 30, 'red': 31, 'green': 32, 'yellow': 33,
          'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37}
def colorize(s, color, bold=False):
    if os.getenv('ANSI_COLORS_DISABLED') is None and color in colors:
        if bold: return '\033[1m\033[%dm%s\033[0m' % (colors[color], s)
        else: return '\033[%dm%s\033[0m' % (colors[color], s)
    else: return s

def rightHightScore():
	src = open("HightScore", "a")
	b = str(score)
	c = str(nbAnnee * 4)
	text = "Le " + date + " le joueur " + pseudo + " a obtenu " + b + " points de victoires en mode " + level + " sur " + c + " saisons"	
	src.write(text)
	src.write('\n\r')
	src.write("-------------------------------------------------------------------------------------------------------------------")
	src.write('\n\r')
	src.close()

def printHightScore():
	src = open("HightScore", "r")
	for ligne in src:
		data = ligne.rstrip('\n\r')
		print data
	src.close()

def plateau_myrmes():
	print colorize('___________________________________________________________________________________________________________________', c, b)
	print ""
	print "TOUR :", tour_de_jeux, "/", (nbAnnee * 4), " |  ANNÉE : ", annee, " |  SAISON :", saison, " |  DIFFICULTÉ :", level
	print colorize('-------------------------------------------------------------------------------------------------------------------', c, b)
	print "NIVEAU FOURMILIÈRE :", niveau_fourmiliere, " |  POINTS DE VICTOIRE :", score
	print colorize('-------------------------------------------------------------------------------------------------------------------', c, b)	
	print "NOURRITURE :", nourriture, " |  TERRE :", terre, " |  BOIS :", bois, " |  PROIES CHASSÉES :", proie
	print colorize('-------------------------------------------------------------------------------------------------------------------', c, b)
	print "LARVES :", larve, " |  NOURRICES :", nourrice, " |  OUVRIÈRES :", ouvriere, " |  SOLDATES :", soldate
	print colorize('-------------------------------------------------------------------------------------------------------------------', c, b)
	print "ÉLEVAGE PUCERONS :", elevage_puceron, " |  FOUILLES :", fouille, " |  EXTENTIONS :", extention
	print colorize('___________________________________________________________________________________________________________________', c, b)

import random
alea_climat = 0
protec_alea_climat_5 = 0
mission_1 = 0
mission_2 = 0

nourrice_t = 0
ouvriere_in1 = 0
ouvriere_in2 = 0
ouvriere_in3 = 0
ouvriere_in4 = 0
proie = 0

compt_saison = 1
compt_annee = 1
tour_de_jeux = 1
annee = 1
couleur = ""

b = True
x = 0
y = 0
z = 0

print colorize('___________________________________________________________________________', 'green', b), "                |     |"
print "                                                                                             \   /"
print "Bienvenue sur", colorize('Myrmes.py', 'magenta', b), "jeux de gestion inspiré du jeu de plateau                             \_/"
print "Vous allez gerer la vie d'une colonie de fourmis a travers les saisons                   __   /^\   __"
print "Chaque année est divisée en 4 saisons (Printemps, Éte, Automne, Hiver)                  '  `. \_/ ,'  `"
print "Prenez garde a l'hiver, pensez à stocker de la nourriture !                                  \/ \/"
print "Essayez d'obtenir le meilleur score. GL & HF ;)                                         _,--./| |\.--._  "
print "___________________________________________________________________________          _,'   _.-\_/-._   `._"
print "___________________________________________________________________________               |   / \   |"
print "                                                                                          |  /   \  |"
print colorize('Myrmes.(R)', 'magenta', b), "est un jeu créé par", colorize('YOANN LEVET', 'magenta', b), "et edité par", colorize('YSTARI GAMES', 'magenta', b), "                    /   |   |   \ "
print colorize('___________________________________________________________________________', 'green', b), "           -'    \___/    `-"
print ""

manuel = int(input("Souhaitez-vous lire le manuel, conseille si 1er partie ? 1=OUI| 0=NON "))
if manuel == 1:
	print "___________________________________________________________________________________________________________________"
	print ""
	print "					Bienvenue dans le MANUEL de MYRMES 2.0"
	print ""
	print "C'EST LA CHRIS QUE TU DOIS ECRIRE LE MANUEL !"
	print "___________________________________________________________________________________________________________________"
	print ""

pseudo = raw_input("Veuillez entrer votre pseudo : ")
print ""

print "Bonjour", colorize(pseudo, 'magenta', b), "!"
print ""

print "Dans", colorize('Myrmes.py', 'magenta', b), "vous pouvez choisir de jouer de", colorize('3', 'blue', b), "à", colorize('15', 'blue', b),  colorize('années', 'magenta', True), "!"
print "Le jeu de plateau original", colorize('Myrmes.(R)', 'magenta', b), "se déroule sur", colorize('3', 'blue', b), colorize('années', 'magenta', b)
print "Combien d'" + colorize('années', 'magenta', b), "souhaitez-vous jouer ?"
while True:
	try:
		nbAnnee = int(raw_input())
		break
	except:
		print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."

if nbAnnee < 3: nbAnnee = 3
if nbAnnee > 15: nbAnnee = 15
print ""

print "Dans", colorize('Myrmes.py', 'magenta', b), "vous pouvez choisir votre", colorize('niveau', 'magenta', b), "de difficulté de", colorize('1', 'blue', b), "à", colorize('5', 'blue', b), "!"
print colorize('1', 'blue', b), ":", colorize('Larve', 'magenta', b), "|", colorize('2', 'blue', b), ":", colorize('Minor', 'magenta', b), "|", colorize('3', 'blue', b), ":", colorize('Media', 'magenta', b), "|",colorize('4', 'blue', b), ":", colorize('Major', 'magenta', b), "|", colorize('5', 'blue', b), ":", colorize('Gyne', 'magenta', b)
print "Le jeu de plateau original", colorize('Myrmes.(R)', 'magenta', b), "se déroule au", colorize('niveau', 'magenta', b), colorize('5', 'blue', b)
print "A quel", colorize('niveau', 'magenta', b), "souhaitez-vous jouer ?"
while True:
	try:
		code = int(raw_input())
		break
	except:
		print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."

if code < 1: code = 1
if code > 5: code = 5

if pseudo == "CHUCK NORRIS":
	larve = 100
	nourrice_save = 100
	ouvriere = 100
	soldate = 100
	nourriture = 100
	terre = 100
	bois = 100
	score = 100
	niveau_fourmiliere = 3
	elevage_puceron = 10
	fouille = 10
	extention = 10
	tour_de_jeux = 1
	mission_1 = 1
	mission_2 = 1
	x= 1
	y = 1
	z = 1
	level = "GOD MOD"

elif pseudo == "NAPOLEON":
	larve = 0
	nourrice_save = 0
	ouvriere = 0
	soldate = 0
	nourriture = 0
	terre = 0
	bois = 0
	score = 1
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "TERRE BRULÉE"

elif code == 5:
	larve = 1
	nourrice_save = 3
	ouvriere = 2
	soldate = 0
	nourriture = 0
	terre = 0
	bois = 0 
	score = 10
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "GYNE"

elif code == 4:
	larve = 2
	nourrice_save = 4
	ouvriere = 3
	soldate = 1
	nourriture = 0
	terre = 0
	bois = 0 
	score = 10
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "MAJOR"

elif code == 3:
	larve = 3
	nourrice_save = 5
	ouvriere = 4
	soldate = 2
	nourriture = 1
	terre = 1
	bois = 1
	score = 10
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "MEDIA"

elif code == 2:
	larve = 4
	nourrice_save = 7
	ouvriere = 5
	soldate = 3
	nourriture = 2
	terre = 2
	bois = 2
	score = 10
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "MINOR"

elif code == 1:
	larve = 5
	nourrice_save = 7
	ouvriere = 6
	soldate = 4
	nourriture = 3
	terre = 3
	bois = 3
	score = 10
	niveau_fourmiliere = 0
	elevage_puceron = 0
	fouille = 0
	extention = 0
	level = "LARVE"

while tour_de_jeux < ((nbAnnee * 4) + 1) and score > 0:

	if compt_annee == 5:
			annee = annee + 1
			compt_annee = 1
	
	if compt_saison == 5:
			compt_saison = 1

	if compt_saison == 1:
		c = 'green'
		saison = colorize('Printemps', c, b)
	elif compt_saison == 2:
		c = 'yellow'
		saison = colorize('Éte', c, b)
	elif compt_saison == 3:
		c = 'red'
		saison = colorize('Automne', c, b)
	elif compt_saison == 4:
		c = 'cyan'
		saison = colorize('Hiver', c, b)

	nourrice = nourrice_save + nourrice_t
	u = 0
	pv_climat = 0
	ressource_pax = 0
	ressource_piq = 0
	soldate_climat = 0
	if alea_climat == 5 and protec_alea_climat_5 == 0: niveau_fourmiliere = niveau_fourmiliere - 1
	protec_alea_climat_5 = 0
	
	
	if niveau_fourmiliere == 1 and x == 0:
		
		print ""
		print "Félicitation ! Votre", colorize('fourmilière', 'magenta', b), "a atteint le", colorize('niveau', 'magenta', b), colorize('1', 'blue', b)
		print ""
		print "=> Vous avez maintenant accés au", colorize('garde-manger', 'magenta', b), "et aux", colorize('élevages de puceron', 'magenta', b)
		print "   - Garde-manger (travaux - phase 3) :", colorize('+1', 'blue', b), colorize('nourriture', 'magenta', b)
		print "   - Élevage de puceron (exploitations - phase 3) :", colorize('-1', 'blue', b), colorize('bois', 'magenta', b), colorize('+1', 'blue', b), colorize('nourriture', 'magenta', b), "/tour"
		print "   - Chaque", colorize('récolte', 'magenta', b), "vous rapportent maintenant", colorize('+2', 'blue', b), colorize('points de victoire', 'magenta', b)
		x = 1
		print ""

	if niveau_fourmiliere == 2 and y ==0:
		
		print ""
		print "Félicitation ! Votre", colorize('fourmilière', 'magenta', b), "a atteint le", colorize('niveau', 'magenta', b), colorize('2', 'blue', b)
		print ""
		print "=> Vous avez maintenant accés a la", colorize('carrière', 'magenta', b), "et aux", colorize('fouilles', 'magenta', b)
		print "   - Carrière (travaux - phase 3) :", colorize('+1', 'blue', b), colorize('bois', 'magenta', b), colorize('+1', 'blue', b), colorize('terre', 'magenta', b)
		print "   - Fouille (exploitations - phase 3) :", colorize('-2', 'red', b), colorize('nourriture', 'magenta', b), "à la construction, puis", colorize('+1', 'blue', b), colorize('terre', 'magenta', b), "et", colorize('+1', 'blue', b), colorize('bois', 'magenta', b), "chaque saison suivante"
		print "   - Chaque", colorize('récolte', 'magenta', b), "vous rapportent maintenant", colorize('+4', 'blue', b), colorize('points de victoire', 'magenta', b)
		y = 1
		print ""
	
	if niveau_fourmiliere == 3 and z == 0:
		
		print ""
		print "Félicitation ! Votre", colorize('fourmilière', 'magenta', b), "a atteint le", colorize('niveau', 'magenta', b), colorize('3', 'blue', b)
		print ""
		print "=> Vous avez maintenant accés a la", colorize('salle royale', 'magenta', b), "et aux", colorize('extentions', 'magenta', b)
		print "   - Loge royale (travaux - phase 3) :", colorize('-1', 'red', b), colorize('nourriture', 'magenta', b), colorize('+1', 'blue', b), colorize('point de victoire', 'magenta', b)
		print "   - Extention (exploitations - phase 3) :", colorize('-1', 'red', b), colorize('nourriture/terre/bois', 'magenta', b), "à la construction, puis", colorize('+2', 'blue', b), colorize('points de victoire', 'magenta', b), "chaque saison suivante"
		print "   - Chaque", colorize('récolte', 'magenta', b), "vous rapportent maintenant", colorize('+6', 'blue', b), colorize('points de victoire', 'magenta', b)
		z = 1
		print ""

	if (tour_de_jeux % 4) == 0:
		
		print ""		
		print "WINTER IS COMMING ! Votre fourmilière entre en", colorize('diapause', 'magenta', b)
		print "  La diapause est un etat de repos hivernal dans laquelle la colonie entre au debut de l'hiver"
		print "  C'est une période d'activité reduite où la colonie se met en pause avant de reprendre l'année suivante" 
		print colorize('-------------------------------------------------------------------------------------------------------------------', c, b)
		print "=> Pour survivre à cet", colorize('hiver', c, b), "vous allez devoir dépenser", colorize((annee + 3), 'red', b), colorize('nourritures', 'magenta', b)
		print ""		
		print " - Si vous ne disposez pas des ressources nécessaire vous perdez", colorize('3', 'red', b), colorize('points de victoire', 'magenta', b), "par", colorize('nourriture', 'magenta', b), "manquante"
		print " - Cependant chaque" , colorize('soldates', 'magenta', b),"dont vous disposez vous permet de réduire de", colorize('1', 'blue', b), "la", colorize('nourriture', 'magenta', b), "à depenser"
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		print "Vous avez", colorize(nourriture, 'blue', b), colorize('nourritures', 'magenta', b), ",", colorize(soldate, 'blue', b), colorize('soldates', 'magenta', b), "et", colorize(score, 'blue', b), colorize('points de victoire', 'magenta', b)
		diapause = (annee + 3) - soldate
		if diapause < 0: diapause = 0
		print "Pour passer l'hiver vous devez depenser",  colorize(diapause, 'blue', b), colorize('nourritures', 'magenta', b)
		nourriture_t = nourriture
		if diapause > nourriture:
			score = score - ((diapause - nourriture)*3)
			nourriture = 0 
		else:
			nourriture = nourriture - diapause
		if diapause > nourriture_t: print "La diapause vide votre stock de nourriture et vous perdez",  colorize(((diapause - nourriture_t)*3), 'red', b), colorize('points de victoire', 'magenta', b), "!"
		else: print "La diapause diminue votre stock de nourriture à", nourriture, "mais vous ne perdez pas de", colorize('points de victoire', 'magenta', b)
		print ""
		print "Presser", colorize('ENTRÉE', 'blue', b), "afin de sortir de", colorize('diapause', 'magenta', b), "!"
		raw_input()

		tour_de_jeux = tour_de_jeux + 1
		compt_saison = compt_saison + 1
		compt_annee = compt_annee + 1
	else:
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		print colorize('                            <<< __  /---------------------\  __ >>>', c, b)
		print colorize('                         >()(_)(__) |-PHASE 1 : ÉVÈNEMENT-| (__)(_)()<', c, b)
		print colorize('                            <<<     \---------------------/     >>>', c, b)
		plateau_myrmes()

		while True:

			alea_climat_t = alea_climat			
			pv_climat = 0
			ressource_pax = 0
			ressource_piq = 0
			soldate_climat = 0
			if alea_climat == 5 and protec_alea_climat_5 == 0: niveau_fourmiliere = niveau_fourmiliere - 1
			protec_alea_climat_5 = 0
			
			while True:
				alea_climat = random.randint(0,8)
				if alea_climat != alea_climat_t: break

			if alea_climat == 1:
				climat = "-/ CHASSE À LA VICTOIRE /-"
				bonus = "Lors de chaque gain de " + colorize('points de victoire', 'magenta', b) + " vous gagnez " + colorize('+1', 'blue', b) + " point supplémentaire"
				pv_climat = 1
			elif alea_climat == 2:
				climat = "-/ BABY-BOOM /-"
				bonus = "Lors de la phase " + colorize('naissance', 'magenta', b) + ", si vous obtenez au moins " + colorize('1', 'blue', b) + " " + colorize('larve', 'magenta', b) + ", vous recevez  " + colorize('+2', 'blue', b) + " " + colorize('larves', 'magenta', b) + " supplémentaires"
			elif alea_climat == 3:
				climat = "-/ ENCORE DU TRAVAIL /-"
				bonus = "Lors de la phase " + colorize('naissance', 'magenta', b) + ", si vous obtenez au moins " + colorize('1', 'blue', b) + " " + colorize('ouvrière', 'magenta', b) + ", vous recevez  " + colorize('+1', 'blue', b) + " " + colorize('ouvrière', 'magenta', b) + " supplémentaire"
			elif alea_climat == 4:
				climat = "-/ SI VIS PACEM, PARA BELLUM /-"
				bonus = "Lors de la phase " + colorize('naissance', 'magenta', b) + ", si vous obtenez au moins " + colorize('1', 'blue', b) + " " + colorize('soldate', 'magenta', b) + ", vous recevez  " + colorize('+1', 'blue', b) + " " + colorize('soldate', 'magenta', b) + " supplémentaire"
			elif alea_climat == 5:
				climat = "-/ MÉTROPOLIS /-"
				bonus = "Jusqu'a la fin de la " + colorize('saison', 'magenta', b) + " votre fourmilière gagne " + colorize('+1', 'blue', b) + " " + colorize('niveau', 'magenta', b) + " (et tous les " + colorize('bonus', 'magenta', b) + " associes)"
				if niveau_fourmiliere < 3: niveau_fourmiliere = niveau_fourmiliere + 1
				else: protec_alea_climat_5 = 1
			elif alea_climat == 6:
				climat = "-/ PIQUE-NIQUE /-"
				bonus = "Si vous realisez au moins " + colorize('1', 'blue', b) + " " + colorize('récolte', 'magenta', b) + ", vous recevez " + colorize('+3', 'blue', b) + " " + colorize('ressources', 'magenta', b) + " aléatoires supplémentaires"
				ressource_piq = 3
			elif alea_climat == 7:
				climat = "-/ PAIX ET PROSPERITÉ /-"
				bonus = "Chaque" + colorize('récolte', 'magenta', b) + "effectuée vous rapporte " + colorize('+1', 'blue', b) + " " + colorize('ressource', 'magenta', b) + " aléatoire supplémentaire"
				ressource_pax = 1
			elif alea_climat == 8:
				climat = "-/ I'M A TIGER /-"
				bonus = "Le nombre de " + colorize('soldate', 'magenta', b) + " requise pour la " + colorize('chasse', 'magenta', b) + " est diminué de" + colorize('1', 'blue', b)
				soldate_climat = 1	
		
			print ""
			print "L'" + colorize('évènement', 'magenta', b), "pour cette saison est", colorize(climat, 'magenta', b), "ce qui vous accorde le bonus :"
			print bonus
			print ""
			if larve == 0:
				print "Vous n'avez plus de", colorize('larve', 'magenta', b), "disponibles. Vous devez conserver cet", colorize('évènement', 'magenta', b), "pour cette saison !"
				break	
			else:
				print "Vous avez", colorize(larve, 'blue', b), colorize('larves', 'magenta', b)
				print "Voulez-vous obtenir un nouvel", colorize('évènement', 'magenta', b), "en échange de", colorize('-1', 'red', b), colorize('larve', 'magenta', b), ": O/Enter"
				u = raw_input()
				if u == "O":
					print colorize('                       ----------------------', c, b)
					larve = larve - 1
				else:
					break
			
		print ""
		print "Presser", colorize('ENTRÉE', 'blue', b), "afin de passer à la phase", colorize('naissance', 'magenta', b), "!"
		raw_input()

		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		print colorize('                            <<< __  /----------------------\  __ >>>', c, b)
		print colorize('                         >()(_)(__) |-PHASE 2 : NAISSANCES-| (__)(_)()<', c, b)
		print colorize('                            <<<     \----------------------/     >>>', c, b)
		plateau_myrmes()
		print ""
		print "Vous pouvez utiliser vos", colorize('nourrices', 'magenta', b), "afin d'obtenir plus de", colorize('larves', 'magenta', b) + ", de", colorize('nourrices', 'magenta', b) + ", d'" + colorize('ouvrières', 'magenta', b), "et de", colorize('soldates', 'magenta', b)
		print "Les", colorize('nourrices', 'magenta', b), "non utilisées partiront à l'atelier (Phase 5)"
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""

		print "Vous avez", colorize(nourrice, 'blue', b), colorize('nourrices', 'magenta', b), "et", colorize(larve, 'blue', b), colorize('larves', 'magenta', b)
		if nourrice < 1:
			print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('larves', 'magenta', b), "!"
		else:
			print "Vous pouvez utiliser", colorize('x', 'blue', b), colorize('nourrices', 'magenta', b), "pour obtenir (", colorize('x', 'blue', b), "+ (", colorize('x', 'blue', b), colorize('- 1', 'red', b), ") )", colorize('larves', 'magenta', b)
			print "Exemples : 1 nourrice => 1 larve | 2 nourrices => 3 larves | 3 nourrices => 5 larves ..."
			print "Combien souhaitez-vous utiliser de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('larves', 'magenta', b), "?"
			while True:
				try:
					larve_sup = int(raw_input())
					break
				except:
					print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			while larve_sup > nourrice:
				print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour cela, nouveau choix ?"
				while True:
					try:
						larve_sup = int(raw_input())
						break
					except:
						print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			if larve_sup <= 0: larve_sup = 0
			if larve_sup >= 1 and alea_climat == 2: larve = larve + 2
			if larve_sup >= 1: larve = larve + (larve_sup + (larve_sup - 1))		
			nourrice = nourrice - larve_sup

		print colorize('                       ----------------------', c, b)
		print "Vous avez", colorize(nourrice, 'blue', b), colorize('nourrices', 'magenta', b) + ",", colorize(larve, 'blue', b), colorize('larves', 'magenta', b), "et", colorize(nourriture, 'blue', b), colorize('nourritures', 'magenta', b)
		if nourrice < 1:
			print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('nourrices', 'magenta', b), "!"
		elif larve < 2:
			print "Vous n'avez pas assez de", colorize('larves', 'magenta', b), "pour obtenir plus de", colorize('nourrices', 'magenta', b), "!"
		elif nourriture < 2:
			print "Vous n'avez pas assez de", colorize('nourritures', 'magenta', b), "pour obtenir plus de", colorize('nourrices', 'magenta', b), "!"
		else:
			print "Vous pouvez utiliser", colorize('x', 'blue', b), colorize('nourrices', 'magenta', b),  colorize('-2', 'red', b), colorize('larves', 'magenta', b), colorize('-2', 'red', b), colorize('nourritures', 'magenta', b), "pour obtenir", colorize('x', 'blue', b), colorize('nourrices', 'magenta', b)
			print "Exemples : 1 nourrice => 1 nourrice | 2 nourrices => 2 nourrices | 3 nourrices => 3 nourrices ..."
			print "Combien souhaitez-vous utiliser de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('nourrices', 'magenta', b), "?"
			while True:
				try:
					nourrice_sup = int(raw_input())
					break
				except:
					print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			while nourrice_sup > nourrice or (nourrice_sup * 2) > nourriture or (nourrice_sup * 2) > larve:
				if nourrice_sup > nourrice:
					print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour cela, nouveau choix ?"
					while True:
						try:
							nourrice_sup = int(raw_input())
							break
						except:
							print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
				if nourrice_sup * 2 > nourriture:
					print "Vous n'avez pas assez de", colorize('nourritures', 'magenta', b), "pour cela, nouveau choix ?"
					while True:
						try:
							nourrice_sup = int(raw_input())
							break
						except:
							print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
				if nourrice_sup * 2 > larve:
					print "Vous n'avez pas assez", colorize('larves', 'magenta', b), "pour cela, nouveau choix ?"
					while True:
						try:
							nourrice_sup = int(raw_input())
							break
						except:
							print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			if nourrice_sup <= 0: nourrice_sup = 0
			nourrice_t = nourrice_t + nourrice_sup
			larve = larve - (nourrice_sup * 2)
			nourriture = nourriture - (nourrice_sup * 2)

		print colorize('                       ----------------------', c, b)
		print "Vous avez", colorize(nourrice, 'blue', b), colorize('nourrices', 'magenta', b), "et", colorize(ouvriere, 'blue', b), colorize('ouvrières', 'magenta', b)
		if nourrice < 2:
			print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour obtenir plus d'" + colorize('ouvrières', 'magenta', b), "!"
		else:
			print "Vous pouvez utiliser", colorize('x', 'blue', b), colorize('nourrices', 'magenta', b), "pour obtenir (", colorize('x', 'blue', b), colorize('- 1', 'red', b), ")", colorize('ouvrières', 'magenta', b)
			print "Exemples : 2 nourrices => 1 ouvrière | 3 nourrices => 2 ouvrières | 4 nourrices => 3 ouvrières ..." 
			print "Combien souhaitez-vous utiliser de", colorize('nourrices', 'magenta', b), "pour obtenir plus d'" + colorize('ouvrières', 'magenta', b), "?"
			while True:
				try:
					ouvriere_sup = int(raw_input())
					break
				except:
					print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			while ouvriere_sup > nourrice:
				print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour cela, nouveau choix ?"
				while True:
					try:
						ouvriere_sup = int(raw_input())
						break
					except:
						print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			if ouvriere_sup < 2: ouvriere_sup = 0
			if ouvriere_sup >= 2 and alea_climat == 3: ouvriere = ouvriere + 1
			if ouvriere_sup != 0: ouvriere = ouvriere + (ouvriere_sup - 1)
			nourrice = nourrice - ouvriere_sup

		print colorize('                       ----------------------', c, b)
		print "Vous avez", colorize(nourrice, 'blue', b), colorize('nourrices', 'magenta', b), "et", colorize(soldate, 'blue', b), colorize('soldates', 'magenta', b)
		if nourrice < 2:
			print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('soldates', 'magenta', b), "!"
		else:
			print "Vous pouvez utiliser", colorize('x', 'blue', b), colorize('nourrices', 'magenta', b), "pour obtenir (", colorize('x', 'blue', b), colorize('/ 2', 'red', b), ")", colorize('soldates', 'magenta', b)
			print "Exemples : 2 nourrices => 1 soldate | 4 nourrices => 2 soldates | 6 nourrices => 3 soldates ..." 
			print "Combien souhaitez-vous utiliser de", colorize('nourrices', 'magenta', b), "pour obtenir plus de", colorize('soldates', 'magenta', b), "?"
			soldate_sup = int(input())
			while soldate_sup > nourrice:
				print "Vous n'avez pas assez de", colorize('nourrices', 'magenta', b), "pour cela, nouveau choix ?"
				soldate_sup = int(input())
			if soldate_sup < 2: soldate_sup = 0
			if soldate_sup >= 2 and alea_climat == 4: soldate = soldate + 1
			if soldate_sup % 2 != 0: soldate_sup = soldate_sup - 1
			if soldate_sup != 0 : soldate = soldate + int(soldate_sup / 2)
			nourrice = nourrice - soldate_sup

		print colorize('                       ----------------------', c, b)
		if nourrice == 0: print "Aucune", colorize('nourrice', 'magenta', b), "ne part à l'" + colorize('atelier', 'magenta', b)
		else: print "Vos", colorize(nourrice, 'magenta', b), colorize('nourrices', 'magenta', b), "restantes partent à l'" + colorize('atelier', 'magenta', b)
		print ""
		print "Presser", colorize('ENTRÉE', 'blue', b), "afin de passer à la phase", colorize('activités', 'magenta', b), "!"
		raw_input()
	
	
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		print colorize('                            <<< __  /---------------------\  __ >>>', c, b)
		print colorize('                         >()(_)(__) |-PHASE 3 : ACTIVITES-| (__)(_)()<', c, b)
		print colorize('                            <<<     \---------------------/     >>>', c, b)
		plateau_myrmes()
		print ""
		print "Vous pouvez utiliser vos", colorize('ouvrières', 'magenta', b), "afin d'obtenir plus de", colorize('nourritures', 'magenta', b) + ", de", colorize('terre', 'magenta', b) + ", de", colorize('bois', 'magenta', b), "et de", colorize('points de victoire', 'magenta', b)
		print "Les activitées possibles sont la", colorize('récolte', 'magenta', b), "de ressources, la", colorize('chasse', 'magenta', b), "d'insectes, le", colorize('travail', 'magenta', b), "à la fourmilière et la création d'" + colorize('exploitation', 'magenta', b)
		print "L'extérieur est un milieu hostile. Les", colorize('ouvrières', 'magenta', b), "sorties en", colorize('récolte', 'magenta', b) + ",", colorize('chasse', 'magenta', b) + ",", colorize('travail', 'magenta', b) + ",", colorize('exploitation', 'magenta', b), "sont perdues et ne reviendront pas au nid"
		print "Cependant après construction, les", colorize('exploitations', 'magenta', b), "restent en jeu et rapportent des", colorize('ressources', 'magenta', b), "jusqu'à la fin de la partie"
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		
		if ouvriere == 0:
			print "Vous n'avez pas d'" + colorize('ouvrière', 'magenta', b), "disponible pour la phase", colorize('activités', 'magenta', b), "!"
		else:		
			print "=> Pour chaque ouvriere envoyee en TRAVAUX a l'interieur vous gagnez :"
			print "   Couveuse       (fourmilière niveau 0) : + 1 larve"
			print "   Garde-manger   (fourmilière niveau 1) : + 1 nourriture"
			print "   Carriere       (fourmilière niveau 2) : + 1 terre + 1 bois"
			print "   Chambre royale (fourmilière niveau 3) : - 1 nouriture + 2 points de victoire"
			print ""
			print "=> Pour chaque ouvriere envoyee en EXPLOITATION a l'exterieur, vous pouvez creer :"
			print "   Elevage de pucerons (fourmilière niveau 1) : - 1 bois + 1 nourriture/tour"
			print "   Fouille             (fourmilière niveau 2) : - 2 nourriture + 1 bois/tour + 1 terre/tour"
			print "   Extention            (fourmilière niveau 3) : - 1 [nourriture/bois/terre] + 2 points de victoire/tour"
			print ""
			print "* L'exterieur est un milieu hostile, les ouvrieres sorties (récolte, chasse et exploitation) ne reviendront pas au nid"
			
			print colorize('___________________________________________________________________________________________________________________', c, b)
			print ""
	
			print "Vous avez", colorize(ouvriere, 'blue', b), colorize('ouvrières', 'magenta', b) + ",", colorize(nourriture, 'blue', b), colorize('nourriture', 'magenta', b) + ",", colorize(terre, 'blue', b), colorize('terre', 'magenta', b) + ",", colorize(bois, 'blue', b), colorize('bois', 'magenta', b), "et", colorize(score, 'blue', b), colorize('points de victoire', 'magenta', b)
				
			print "Chaque", colorize('ouvrière', 'magenta', b), "envoyée en", colorize('récolte', 'magenta', b), "vous rapporte", colorize((niveau_fourmiliere + 2), 'blue', b), colorize('ressources', 'blue', b), "aléatoires (dont au moins", colorize('1', 'blue', b), colorize('nourriture', 'magenta', b) + ") ainsi que", colorize((niveau_fourmiliere * 2), 'blue', b), colorize('points de victoire', 'magenta', b)

			print "Combien souhaitez-vous envoyer d'" + colorize('ouvrière', 'magenta', b), "en", colorize('récolte', 'magenta', b), "?"
			while True:
				try:
					ouvriere_rec = int(raw_input())
					break
				except:
					print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
			while ouvriere_rec > ouvriere:
				print "Vous n'avez pas assez d'" + colorize('ouvrière', 'magenta', b), "pour cela, nouveau choix ?"
				while True:
					try:
						ouvriere_rec = int(raw_input())
						break
					except:
						print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."

			if ouvriere_rec <= 0: ouvriere_rec = 0
			ouvriere = ouvriere - ouvriere_rec
			score = score + ouvriere_rec * ((niveau_fourmiliere * 2) + pv_climat)
			nourriture = nourriture + ouvriere_rec
			i = 0
			while i < ((ouvriere_rec * (niveau_fourmiliere + ressource_pax + 1)) + ressource_piq):
				alea_ressource = random.randint(0,3)
				if alea_ressource == 1: nourriture = nourriture + 1
				if alea_ressource == 2: terre = terre + 1
				if alea_ressource == 3: bois = bois + 1
				i = i + 1

			print colorize('                       ----------------------', c, b)
			print "Vous avez", colorize(ouvriere, 'blue', b), colorize('ouvrières', 'magenta', b) + ",", colorize(soldate, 'blue', b), colorize('soldates', 'magenta', b) + ",", colorize(nourriture, 'blue', b), colorize('nourritures', 'magenta', b), "et", colorize(score, 'blue', b), colorize('points de victoire', 'magenta', b)
			print ""

			if ouvriere == 0:
				print "Vous n'avez plus d'" + colorize('ouvrière', 'magenta', b), "disponible pour la", colorize('chasse', 'magenta', b), "!"

			elif (soldate + soldate_climat) == 0:
				print "Vous n'avez plus de" + colorize('soldate', 'magenta', b), "disponible pour la", colorize('chasse', 'magenta', b), "!"

			else:
				print "Chaque", colorize('ouvrière', 'magenta', b), "envoyée en", colorize('chasse', 'magenta', b), "vous rapporte, en fonction de la", colorize('proie', 'magenta', b), " chassée:"
				print colorize('Coccinelle', 'magenta', b), "=>", colorize("+2", 'blue', b), colorize('nourriture', 'magenta', b), colorize(soldate_climat - 1, 'red', b), colorize('soldate', 'magenta', b)
				print colorize('Termite', 'magenta', b), "   =>", colorize("+1", 'blue', b), colorize('nourriture', 'magenta', b), colorize(soldate_climat - 1, 'red', b), colorize('soldate', 'magenta', b), colorize("+1", 'blue', b), colorize('point de victoire', 'magenta', b)
				print colorize('Araignée', 'magenta', b), "  =>", colorize("+1", 'blue', b), colorize('nourriture', 'magenta', b), colorize(soldate_climat - 2, 'red', b), colorize('soldates', 'magenta', b), colorize("+4", 'blue', b), colorize('points de victoire', 'magenta', b)
				print ""
				print "Combien souhaitez-vous envoyer d'" + colorize('ouvrières', 'magenta', b), "à la chasse à la coccinelle ?"

				while True:
					try:
						ouvriere_hunt1 = int(raw_input())
						break
					except:
						print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
				while ouvriere_hunt1 > ouvriere or ouvriere_hunt1 > (soldate + (ouvriere_hunt1 * soldate_climat)):
					if ouvriere_hunt1 > ouvriere:
						print "Vous n'avez pas assez d'" + colorize('ouvrière', 'magenta', b), "pour cela, nouveau choix ?"
						while True:
							try:
								ouvriere_hunt1 = int(raw_input())
								break
							except:
								print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."
					if ouvriere_hunt1 > soldate + (ouvriere_hunt1 * soldate_climat):
						print "Vous n'avez pas assez de", colorize('soldate', 'magenta', b), "pour cela, nouveau choix ?"
						while True:
							try:
								ouvriere_hunt1 = int(raw_input())
								break
							except:
								print "Veuillez saisir un", colorize('nombre', 'magenta', b), colorize('entier', 'magenta', b) + "..."

				if ouvriere_hunt1 <= 0: ouvriere_hunt1 = 0	
				ouvriere = ouvriere - ouvriere_hunt1
				soldate = soldate - ouvriere_hunt1 + (ouvriere_hunt1 * soldate_climat)
				nourriture = nourriture + (ouvriere_hunt1 * 2)
				proie = proie + ouvriere_hunt1
		
			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres et ", soldate, " soldates"
			if ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour chasser des termites !"
			elif (soldate + soldate_climat) == 0:
				print "Vous n'avez plus de soldate pour chasser des termites !"
			else:
				ouvriere_hunt2 =  int(input("Combien souhaitez-vous envoyer d'ouvriere a la chasse de termite ? "))
				while ouvriere_hunt2 > ouvriere or ouvriere_hunt2 > soldate + (ouvriere_hunt2 * soldate_climat):
					if ouvriere_hunt2 > ouvriere:
						ouvriere_hunt2 = int(input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if ouvriere_hunt2 > soldate + (ouvriere_hunt2 * soldate_climat):
						ouvriere_hunt2 =  int(input("Vous n'avez pas assez de soldates pour cela, nouveau choix ? "))		
				if ouvriere_hunt2 < 0: ouvriere_hunt2 = 0		
				ouvriere = ouvriere - ouvriere_hunt2
				soldate = soldate - ouvriere_hunt2 + (ouvriere_hunt2 * soldate_climat)
				score = score + (ouvriere_hunt2 * 2) + pv_climat
				nourriture = nourriture + ouvriere_hunt2
				proie = proie + ouvriere_hunt2

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres et ", soldate, " soldates"
			if ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour chasser des araignees !"
			elif (soldate + soldate_climat) < 2:
				print "Vous n'avez plus assez de soldate pour chasser des araignees !"
			else:
				ouvriere_hunt3 =  int(input("Combien souhaitez-vous envoyer d'ouvriere a la chasse araignee ? "))
				while ouvriere_hunt3 > ouvriere or (ouvriere_hunt3 * 2) > soldate + (ouvriere_hunt3 * soldate_climat):
					if ouvriere_hunt3 > ouvriere:
						ouvriere_hunt3 =  int(input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if (ouvriere_hunt3 * 2) > soldate + (ouvriere_hunt3 * soldate_climat):
						ouvriere_hunt3 =  int(input("Vous n'avez pas assez de soldates pour cela, nouveau choix ? "))
				if ouvriere_hunt3 < 0: ouvriere_hunt3 = 0	
				ouvriere = ouvriere - ouvriere_hunt3
				soldate = soldate - (ouvriere_hunt3 * 2) + (ouvriere_hunt3 * soldate_climat)
				score = score + (ouvriere_hunt3 * 4) + pv_climat
				nourriture = nourriture + ouvriere_hunt3
				proie = proie + ouvriere_hunt3

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres et", larve, "larves"
			if ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour la couveuse !"
			else:
				print "Vous pouvez assigner jusqu'a", annee, "ouvrieres dans cette loge"
				ouvriere_in1 =  int(input("Combien souhaitez-vous assigner d'ouvriere a la couveuse ? "))
				while ouvriere_in1 > ouvriere or ouvriere_in1 > annee:
					if ouvriere_in1 > ouvriere:
						ouvriere_in1 =  int(input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if ouvriere_in1 > annee:
						ouvriere_in1 =  int(input("Vos loges sont trop petites pour cela, nouveau choix ? "))
				if ouvriere_in1 < 0: ouvriere_in1 = 0
				ouvriere = ouvriere - ouvriere_in1
				larve = larve + ouvriere_in1

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres et", nourriture, "nourritures"
			if niveau_fourmiliere < 1:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder au garde-manger !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour le garde-manger !"
			else:
				print "Vous pouvez assigner jusqu'a", annee, "ouvrieres dans cette loge"
				ouvriere_in2 =  int(input("Combien souhaitez-vous assigner d'ouvriere a la garde-manger ? "))
				while ouvriere_in2 > ouvriere or ouvriere_in2 > annee:
					if ouvriere_in2 > ouvriere:
						ouvriere_in2 =  int(input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if ouvriere_in2 > annee:
						ouvriere_in2 =  int(input("Vos loges sont trop petites pour cela, nouveau choix ? "))
				if ouvriere_in2 < 0: ouvriere_in2 = 0
				ouvriere = ouvriere - ouvriere_in2
				nourriture = nourriture + ouvriere_in2

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres,", terre, "terre et", bois, "bois"
			if niveau_fourmiliere < 2:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder a la carriere !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour la carriere !"
			else:
				print "Vous pouvez assigner jusqu'a", annee, "ouvrieres dans cette loge"
				ouvriere_in3 =  int(input("Combien souhaitez-vous assigner d'ouvriere a la carriere ? "))
				while ouvriere_in3 > ouvriere or ouvriere_in3 > annee:
					if ouvriere_in3 > ouvriere:
						ouvriere_in3 =  int(input("vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if ouvriere_in3 > annee:
						ouvriere_in3 =  int(input("Vos loges sont trop petites pour cela, nouveau choix ? "))
				if ouvriere_in3 < 0: ouvriere_in3 = 0
				ouvriere = ouvriere - ouvriere_in3
				terre = terre + ouvriere_in3
				bois = bois + ouvriere_in3
	
			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres,", nourriture, "nourriture et", score, "points de victoire"
			if niveau_fourmiliere < 3:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder a la loge royale !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour la loge royale !"
			elif nourriture == 0:
				print "Vous n'avez plus de nourriture pour la loge royale !"
			else:
				print "Vous pouvez assigner jusqu'a", annee, "ouvrieres dans cette loge"
				ouvriere_in4 =  int(input("Combien souhaitez-vous assigner d'ouvriere a la loge royale ? "))
				while ouvriere_in4 > ouvriere or ouvriere_in4 > nourriture or ouvriere_in4 > annee:
					if ouvriere_in4 > ouvriere:
						ouvriere_in4 =  int(input("vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? "))
					if ouvriere_in4 > nourriture:
						ouvriere_in4 =  int(input("Vous n'avez pas assez de nourritures pour cela, nouveau choix ? "))
					if ouvriere_in4 > annee:
						ouvriere_in4 =  int(input("Vos loges sont trop petites pour cela, nouveau choix ? "))
				if ouvriere_in4 < 0: ouvriere_in4 = 0
				ouvriere = ouvriere - ouvriere_in4
				nourriture = nourriture - ouvriere_in4
				score = score + (ouvriere_in4 * 2) + pv_climat

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres,", bois, "bois et", elevage_puceron, "elevages de pucerons"
			if niveau_fourmiliere < 1:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder aux elevages de pucerons !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour creer un elevage de pucerons !"
			else:
				elevage_new =  input("Combien souhaitez-vous assigner d'ouvriere a la creation de nouvels elevages de pucerons ? ")
				while elevage_new > ouvriere or elevage_new > bois:
					if elevage_new > ouvriere:
						elevage_new =  input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? ")
					if elevage_new > bois:
						elevage_new =  input("Vous n'avez pas assez de bois pour cela, nouveau choix ? ")
				if elevage_new < 0: elevage_new = 0
				bois = bois - int(elevage_new)
				ouvriere = ouvriere - int(elevage_new)
				elevage_puceron = elevage_puceron + int(elevage_new)

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres,", nourriture, "nourritures et", fouille, "fouilles"
			if niveau_fourmiliere < 2:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder aux fouilles !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour creer une fouille !"
			else:
				fouille_new =  input("Combien souhaitez-vous assigner d'ouvriere a la creation de nouvelles fouilles ? ")
				while fouille_new > ouvriere or (fouille_new * 2) > nourriture:
					if fouille_new > ouvriere:
						fouille_new =  input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? ")
					if (fouille_new * 2) > nourriture:
						fouille_new =  input("Vous n'avez pas assez de nourriture pour cela, nouveau choix ? ")
				if fouille_new < 0: fouille_new = 0
				nourriture = nourriture - (int(fouille_new) * 2)
				ouvriere = ouvriere - int(fouille_new)
				fouille = fouille + int(fouille_new)

			print colorize('                       ----------------------', c, b)
			print "Vous avez", ouvriere, " ouvrieres,", nourriture, "nourritures,", terre, "terre,", bois, "bois et", extention, "extentions"
			if niveau_fourmiliere < 3:
				print "Vous n'avez pas atteint le niveau necessaire pour acceder aux extentions !"
			elif ouvriere == 0:
				print "Vous n'avez plus d'ouvriere pour creer une extention !"
			else:
				extention_new =  input("Combien souhaitez-vous assigner d'ouvriere a la creation d'une extention ? ")
				while extention_new > ouvriere or extention_new > nourriture or extention_new > terre or extention_new > bois:
					if extention_new > ouvriere:
						extention_new =  input("Vous n'avez pas assez d'ouvrieres pour cela, nouveau choix ? ")
					if extention_new > nourriture:
						extention_new =  input("Vous n'avez pas assez de nourriture pour cela, nouveau choix ? ")
					if extention_new > terre:
						extention_new =  input("Vous n'avez pas assez de terre pour cela, nouveau choix ? ")
					if extention_new > bois:
						extention_new =  input("Vous n'avez pas assez de bois pour cela, nouveau choix ? ")
				if extention_new < 0: extention_new = 0
				nourriture = nourriture - int(extention_new)
				bois = bois - int(extention_new)
				terre = terre - int(extention_new)
				ouvriere = ouvriere - int(extention_new)
				extention = extention + int(extention_new)

			nourriture = nourriture + elevage_puceron
			bois = bois + fouille
			terre = terre + fouille
			score = score + (extention * 2) + pv_climat
			ouvriere = ouvriere + int(ouvriere_in1) + int(ouvriere_in2) + int(ouvriere_in3) + int(ouvriere_in4)
	

		
		print ""
		print "Vous pouvez récuperer 1 nourriture supplémentaire en sacrifiant 3 de vos larves"
		u = input ("Sacrifier 3 larves pour obtenir 1 nourriture ? 1:OUI | 0:NON ")
		if u == 1:
			larve = larve - 3
			nourriture = nourriture +1
		
		print ""
		print "Presser", colorize('ENTRÉE', 'blue', b), "afin de passer à la phase", colorize('atelier', 'magenta', b), "!"
		raw_input()
		
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""
		print colorize('                            <<< __  /-------------------\  __ >>>', c, b)
		print colorize('                         >()(_)(__) |-PHASE 4 : ATELIER-| (__)(_)()<', c, b)
		print colorize('                            <<<     \-------------------/     >>>', c, b)
		print colorize('___________________________________________________________________________________________________________________', c, b)
		print ""

		if nourrice == 0:
			print "Vous n'avez pas de nourrice à l'atelier"
		else:
			print colorize('___________________________________________________________________________________________________________________', c, b)
			print ""
			print "* Vous etes maintenant dans l'atelier *"
			print "Vous pouvez y utiliser vos ", nourrice, " nourrices restantes pour :"
			print ""
			print "=> Ameliorer votre foumilliere :"
			print "   fourmilière niveau 1 : - 2 terre"
			print "   fourmilière niveau 2 : - 2 terre - 1 bois"
			print "   fourmilière niveau 3 : - 3 bois"
			print ""
			print "=> Reussir une des missions proposees (!BETA!)"
			print " - mission de niveau 1 : + 6 points de victoires"
			print " - mission de niveau 2 : + 9 points de victoires"
			print " - mission de niveau 3 : + 12 points de victoires"
			print "   Chaque mission necessite 1 nourrice"
			print colorize('___________________________________________________________________________________________________________________', c, b)
			print ""
	
			print "Votre fourmilière est de niveau", niveau_fourmiliere
			if niveau_fourmiliere == 3:
				print "Votre fourmilière a deja atteint le niveau maximum !"	

			elif nourrice == 0:
				print "Vous avez", nourrice, "nourrices, ", terre, "terre et", bois, "bois"
				print "Vous n'avez plus de nourrices pour ameliorer votre fourmilière !"

			elif niveau_fourmiliere == 2 and bois >= 3:
				print "Vous avez", nourrice," nourrices,", terre, "terre et", bois, "bois"
				reponse_niv_3 = input("Souhaitez-vous ameliorer votre fourmilière au niveau 3 ? 1=OUI | 0=NON ")
				if reponse_niv_3 == 1:
					niveau_fourmiliere = 3
					nourrice = nourrice - 1
					terre = terre - 2

			elif niveau_fourmiliere == 1 and terre >= 2 and bois >= 1:
				print "Vous avez", nourrice, "nourrices,", terre, "terre et", bois, " bois"
				reponse_niv_2 = input("Souhaitez-vous ameliorer votre fourmilière au niveau 2 ? 1=OUI | 0=NON ")
				if reponse_niv_2 == 1:
					niveau_fourmiliere = 2
					nourrice = nourrice - 1
					terre = terre - 2
					bois = bois - 1

			elif niveau_fourmiliere == 0 and terre >= 2:
				print "Vous avez", nourrice, "nourrices,", terre, "terre et", bois, "bois"
				reponse_niv_1 = input("Souhaitez-vous ameliorer votre fourmilière au niveau 1 ? 1=OUI | 0=NON ")
				if reponse_niv_1 == 1: 
					niveau_fourmiliere = 1
					nourrice = nourrice - 1
					bois = bois - 3
			else:
				print "Vous avez", nourrice, "nourrices, ", terre, "terre et ", bois, "bois"
				print "Vous n'avez pas les ressources necessaires pour ameliorer votre fourmilière !"


			print colorize('                       ----------------------', c, b)
			etat_mission = 0
			reward_mission = 0
			if nourrice == 0:
				print "Vous n'avez plus de nourrices pour disponibles pour les missions !"
			else:
				u = input("Souhaitez-vous relevez une mission ? 1=OUI | 0=NON ")
				if u == 1:
					print ""
					print "=> Vous avez acces aux missions de niveau 1 :"
					print "   #1 : - 3 nourritures"
					print "   #2 : - 5 larves"
					print "   #3 : - 2 soldates"
					print "   #4 : - 2 proies"
					print "   #5 : - 1 exploitation sur au moins 2"

					if mission_1 == 1:
						print ""
						print "=> Vous avez acces aux missions de niveau 2 :"
						print "   #6 : - 6 terres"
						print "   #7 : - 9 larves"
						print "   #8 : - 3 proies"
						print "   #9 : - 1 nourrice sur au moins 6"
						print "  #10 : - 1 niveau de fourmilière si niveau 2"

					if mission_2 == 1:
						print ""
						print "=> Vous avez acces aux missions de niveau 3 :"
						print "   #11 : - 9 bois"
						print "   #12 : - 4 proies"
						print "   #13 : - 2 nourrices sur au moins 8"
						print "   #14 : - 2 exploitation sur au moins 3"
						print "   #15 : - 2 niveaux de fourmilière si niveau 3"

					print ""
					mission = input("Selectionnez le # de la mission que vous souhaitez realiser ? ")
					if mission == 1 and nourriture >= 3:
						nourriture = nourriture - 3
						etat_mission = 1
						reward_mission = 6
						score = score + reward_mission
						mission_1 = 1
					if mission == 2 and larve >= 5:
						larve = larve - 5
						etat_mission = 1
						reward_mission = 6
						score = score + reward_mission
						mission_1 = 1
					if mission == 3 and soldate >= 2:
						soldate = soldate - 2
						etat_mission = 1
						reward_mission = 6
						score = score + reward_mission
						mission_1 = 1
					if mission == 4 and proie >= 2:
						proie = proie - 2
						etat_mission = 1
						reward_mission = 6
						score = score + reward_mission
						mission_1 = 1
					if mission == 5 and (niveau_fourmiliere + fouille + extention) >= 2:
						u = 0						
						while u < 1:
							alea_mission_1 = 4						
							while alea_mission_1 > 3:
								alea_mission_1 = int(random.random()*10)+1
							if alea_mission_1 == 1 and niveau_fourmiliere > 1:
								niveau_fourmiliere = niveau_fourmiliere - 1
								u = 1
							if alea_mission_1 == 2 and fouille > 1:
								fouille = fouille - 1
								u = 1
							if alea_mission_1 == 3 and extention > 1:
								extention = extention - 1
								u = 1
							etat_mission = 1
							reward_mission = 6
							score = score + reward_mission
							mission_1 = 1


					if mission == 6 and terre >= 6:
						terre = terre - 6
						etat_mission = 1
						reward_mission = 9
						score = score + reward_mission
						mission_2 = 1
					if mission == 7 and larve >= 9:
						larve = larve - 9
						etat_mission = 1
						reward_mission = 9
						score = score + reward_mission
						mission_2 = 1
					if mission == 8 and proie >= 3:
						proie = proie - 3
						etat_mission = 1
						reward_mission = 9
						score = score + reward_mission
						mission_2 = 1
					if mission == 9 and nourrice >= 6:
						nourrice = nourrice - 1
						etat_mission = 1
						reward_mission = 9
						score = score + reward_mission
						mission_2 = 1
					if mission == 10 and niveau_fourmiliere == 2:
						niveau_fourmiliere = 1
						etat_mission = 1
						reward_mission = 9
						score = score + reward_mission
						mission_2 = 1


					if mission == 11 and bois >= 9:
						bois = bois - 9
						etat_mission = 1
						reward_mission = 12
						score = score + reward_mission
					if mission == 12 and proie >= 4:
						proie = proie - 4
						etat_mission = 1
						reward_mission = 12
						score = score + reward_mission
					if mission == 13 and nourrice >= 8:
						nourrice = nourrice - 2
						etat_mission = 1
						reward_mission = 12
						score = score + reward_mission
					if mission == 14 and (niveau_fourmiliere + fouille + extention) >= 3:
						u = 0						
						while u < 2:
							alea_mission_2 = 4
							while alea_mission_2 > 3:
								alea_mission_2 = int(random.random()*10)+1
							if alea_mission_2 == 1 and niveau_fourmiliere > 1:
								niveau_fourmiliere = niveau_fourmiliere - 1
								u = u + 1
							if alea_mission_2 == 2 and fouille > 1:
								fouille = fouille - 1
								u = u + 1
							if alea_mission_2 == 3 and extention > 1:
								extention = extention - 1
								u = u + 1
							etat_mission = 1
							reward_mission = 6
							score = score + reward_mission
							mission_1 = 1
					if mission == 15 and niveau_fourmiliere >= 3:
						niveau_fourmiliere = 1
						etat_mission = 1
						reward_mission = 12
						score = score + reward_mission
						
					print ""
					if etat_mission == 0: print "Echec de la mission, vous ne remplissiez pas les conditions requises !"
					else: print "Succes de la mission, vous gagnez", reward_mission, "points de victoires"

		print ""
		u = input("Taper 1 puis ENTREE afin de passer a l'annee suivante... ")

		tour_de_jeux = tour_de_jeux + 1
		compt_saison = compt_saison + 1
		compt_annee = compt_annee + 1

if score <= 0:
	print colorize("""___________________________________________________________________________________________________________________
               ____ ____ ____   (             (                (                        ____ ____ ____ 
              |   /|   /|   /   )\ )          )\ )     (       )\ )    *   )           |   /|   /|   / 
              |  / |  / |  /   (()/(    (    (()/(     )\     (()/(  ` )  /(   (       |  / |  / |  /  
              | /  | /  | /     /(_))   )\    /(_)) ((((_)(    /(_))  ( )(_))  )\      | /  | /  | /   
              |/   |/   |/     (_))_   ((_)  (_))_|  )\ _ )\  (_))   (_(_())  ((_)     |/   |/   |/    
             (    (    (        |   \  | __| | |_    (_)_\(_) |_ _|  |_   _|  | __|   (    (    (      
             )\   )\   )\       | |) | | _|  | __|    / _ \    | |     | |    | _|    )\   )\   )\     
            ((_) ((_) ((_)      |___/  |___| |_|     /_/ \_\  |___|    |_|    |___|  ((_) ((_) ((_)
___________________________________________________________________________________________________________________""", 'red', True)
	print ""
	print "* Votre fourmilière n'a pas survecu a l'hiver en difficulte :", level, "..."
	print ""
	if code == 0: print "=> Peut-etre devriez-vous essayer le mode de difficulte inferrieur :p"
	else: print "=> Relisez le manuel, assimilez les regles, optimisez votre strategie et retentez votre chance !"
	print colorize('___________________________________________________________________________________________________________________', 'red', True)
	print ""
	print "Voir tableau des scores ? O/n"
	u = raw_input()
	if u == "O":
		print colorize('___________________________________________________________________________________________________________________', 'blue', True)
		print ""
		printHightScore()
	print colorize('___________________________________________________________________________________________________________________', 'blue', True)
	print ""

else:
	print colorize("""___________________________________________________________________________________________________________________
   _  _  _                _________   _______   _________   _______   _________   _______    _______      _  _  _ 
  ( )( )( )    |\     /|  \__   __/  (  ____ \  \__   __/  (  ___  )  \__   __/  (  ____ )  (  ____ \    ( )( )( )
  | || || |    | )   ( |     ) (     | (    \/     ) (     | (   ) |     ) (     | (    )|  | (    \/    | || || |
  | || || |    | |   | |     | |     | |           | |     | |   | |     | |     | (____)|  | (__        | || || |
  | || || |    ( (   ) )     | |     | |           | |     | |   | |     | |     |     __)  |  __)       | || || |
  (_)(_)(_)     \ \_/ /      | |     | |           | |     | |   | |     | |     | (\ (     | (          (_)(_)(_)
   _  _  _       \   /    ___) (___  | (____/\     | |     | (___) |  ___) (___  | ) \ \__  | (____/\     _  _  _ 
  (_)(_)(_)       \_/     \_______/  (_______/     )_(     (_______)  \_______/  |/   \__/  (_______/    (_)(_)(_)
___________________________________________________________________________________________________________________""", 'blue', True)
	print ""
	print " ***  Votre fourmilière a survecu durant ", (nbAnnee * 4), "saisons !  ***"
	print ""
	print " ***  Vous avez gagnez ", score, " points de victoire en difficulte :", level, " ***"
	print ""
	rightHightScore()
	if code < 5: print "=> C'est pas mal, maintenant essayez de survivre au mode de difficulte superrieur :p"
	else: print "=> C'est pas mal, mais si vous optimisez votre strategie vous pouvez obtenir un meilleur score ;)"
	print colorize('___________________________________________________________________________________________________________________', 'blue', True)
	print ""
	print "Voir tableau des scores ? O/n"
	u = raw_input()
	if u == "O":
		print colorize('___________________________________________________________________________________________________________________', 'blue', True)
		print ""
		printHightScore()
	print colorize('___________________________________________________________________________________________________________________', 'blue', True)
	print ""






