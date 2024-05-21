
import pygame
from pathlib import Path
import json
import sys

#SCREEN
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 200


''' -- PYGAME -- '''
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Py App Launcher')



''' -- LOOP -- '''
run = True
while run:
    pygame.draw.rect(screen, 'red', [10, 10, 100, 70])
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()