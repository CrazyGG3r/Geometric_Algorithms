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

#menu text
headin = c.Text("Geometric Algorithms",cm.fonts[0],36,(100,100,150),320,90)
dot = c.point(0,0,(50,50,50),5)
dot_interval = 1000
last_dot_time = 0
screen.fill(background)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = pygame.time.get_ticks()
    if current_time - last_dot_time > dot_interval:
        dot.update_coords((r.randint(0,width),r.randint(0,height)))
        dot.draw(screen)
        last_dot_time = current_time
        # Add a random dot
    mouse = pygame.mouse.get_pos()
    print(mouse)
    
    tr.erasetrail(screen,background)
    tr.updatetrail(mouse)
    tr.drawtrail(screen)
    headin.draw(screen)
    pygame.display.flip()

    clock.tick(60)


