# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 01:51:57 2024

@author: Pr. TAC_MACHINO
"""

import pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
window = pygame.display.set_mode((800, 600))

# Boucle principale du jeu
running = True
while running:
    # Gestion des événements
    for event in pygame.event.get():
        # Si l'utilisateur ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
        
        # Si l'utilisateur clique avec la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Récupérer les coordonnées du clic
            previous_mouse_pos = pygame.mouse.get_pos()
            print("Clic effectué à la position", previous_mouse_pos)
            
            # Dessin d'un point vert au point où la souris est cliquée
            pygame.draw.circle(window, (0, 255, 0), previous_mouse_pos, 3)
            
        # Si l'utilisateur relâche le clic de souris
        if event.type == pygame.MOUSEBUTTONUP:
            # Récupérer les coordonnées du relâchement du clic
            current_mouse_pos = pygame.mouse.get_pos()
            print("Clic relaché à la position ", current_mouse_pos)
            
            # dessin d'un point rouge au point où la souris a été relaché
            pygame.draw.circle(window, (255, 0, 0), current_mouse_pos, 3)
        
            if previous_mouse_pos is not None:
                # Comparer les coordonnées pour déterminer la direction
                if current_mouse_pos[0] > previous_mouse_pos[0]:
                    print("La souris a été déplacée vers la droite")
                elif current_mouse_pos[0] < previous_mouse_pos[0]:
                    print("La souris a été déplacée vers la gauche")
                
                if current_mouse_pos[1] > previous_mouse_pos[1]:
                    print("La souris a été déplacée vers le bas")
                elif current_mouse_pos[1] < previous_mouse_pos[1]:
                    print("La souris a été déplacée vers le haut")
                
            pygame.draw.line(window, (255, 255, 255), previous_mouse_pos, current_mouse_pos)
            previous_mouse_pos = None
            
    # Mise à jour de l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()

