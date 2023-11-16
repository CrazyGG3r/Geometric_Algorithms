from pickle import FALSE
import pygame
import sys
import CLASSES as c
import random as r
import CONVEXHULL as cv 
import cosmetics as cm
from functools import cmp_to_key

#pygame kachra =-=-=-=--=-=-
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
background =(24, 3, 82)



#mouse effects
firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
tr = c.trail(firstset,7)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background)
    mouse = pygame.mouse.get_pos()
    print(mouse)
    tr.erasetrail(screen,background)
    tr.updatetrail(mouse)
    tr.drawtrail(screen)
    pygame.display.flip()

    clock.tick(60)


