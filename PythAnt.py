# -*- coding: cp1252 -*-

import pygame # importation de la librairie pygame

blue = (113,177,227) # canaux Red Green Blue
white = (255,255,255) # valeur max = 255

pygame.init() # initialisation de pygame

surfaceW = 800 # d�finition de la largeur
surfaceH = 500 # d�finition de la hauteur

surface = pygame.display.set_mode((surfaceW,surfaceH)) # cr�ation de la fen�tre WxH
pygame.display.set_caption("PythAnt") # d�nomination de la fen�tre

game_over = False # variable de fin de jeux -> faux

while not game_over: # boucle, tant que game_over est vrai, v�rifier la event, si event QUIT, game_over -> vrai
    for event in pygame.event.get():
        if event.key == pygame.QUIT:
            game_over = True
            
    surface.fill(blue) # m�thode de colorisation de la fen�tre

    pygame.display.update() # rafraichir la fen�tre


pygame.quit() # fermer le module pygame
quit() # fermer le programme
