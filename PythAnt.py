# -*- coding: cp1252 -*-

import pygame # importation de la librairie pygame

blue = (113,177,227) # canaux Red Green Blue
white = (255,255,255) # valeur max = 255

pygame.init() # initialisation de pygame

surfaceW = 800 # définition de la largeur
surfaceH = 500 # définition de la hauteur

surface = pygame.display.set_mode((surfaceW,surfaceH)) # création de la fenêtre WxH
pygame.display.set_caption("PythAnt") # dénomination de la fenêtre

game_over = False # variable de fin de jeux -> faux

while not game_over: # boucle, tant que game_over est vrai, vérifier la event, si event QUIT, game_over -> vrai
    for event in pygame.event.get():
        if event.key == pygame.QUIT:
            game_over = True
            
    surface.fill(blue) # méthode de colorisation de la fenêtre

    pygame.display.update() # rafraichir la fenêtre


pygame.quit() # fermer le module pygame
quit() # fermer le programme
