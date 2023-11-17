from asyncio.windows_events import NULL
from os import abort
from pickle import FALSE
from numpy import False_
import pygame
import sys
import CLASSES as c
import random as r
import CONVEXHULL as cv 
import cosmetics as cm
import convexhullpage as cvhp
from functools import cmp_to_key

#pygame kachra =-=-=-=--=-=-
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()
background =(0,15,15)



#mouse effects
firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
tr = c.trail(firstset,7)

#menu text
hcolor = (0,158,158)
headin = c.Text("Geometric Algorithms",cm.fonts[0],50,hcolor,320,90)
dot = c.point(0,0,(0,40,40),5)
dot_interval = 500
last_dot_time = 0
l = c.line(1,10,(50,50,50))
screen.fill(background)

def ext():
    abort()
#buttons
def dummdumm(screen = NULL):
    print("dumdum")
b1 = 535
b2 = 180
o = 35
buttoncolor = (0,170,170)

button0 = c.Button("Set Points"       ,b1,b2      ,150,25,cm.fonts[0],20,buttoncolor,dummdumm)
button1 = c.Button("Convex Hull"      ,b1,b2+(o*1),150,25,cm.fonts[0],20,buttoncolor,cvhp.conv)
button2 = c.Button("Line Intersection",b1,b2+(o*2),170,25,cm.fonts[0],20,buttoncolor,dummdumm)
button3 = c.Button("Credits"          ,b1,b2+(o*3),130,25,cm.fonts[0],20,buttoncolor,dummdumm)
button4 = c.Button("Exit"             ,b1,b2+(o*4),130,25,cm.fonts[0],20,buttoncolor,dummdumm)
butt = [button0,button1,button2,button3,button4] 
inmenu =0
while running:
    print("menu")
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button
            for a in butt:           
                a.is_hovered = a.x < event.pos[0] < a.x + a.width and a.y < event.pos[1] < a.y + a.height
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            for a in butt:
                if a.is_hovered:
                   a.is_clicked = True
    
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Check if the left mouse button is released
            for a in butt:
                if a.is_clicked:
                    a.is_clicked = False
                    print("Reached")
                    screen.fill((0,10,10))
                    inmenu = 0
                    a.action(screen)      
    #for n,a in enumerate(butt):
    #    print(n,a.is_hovered,a.is_clicked)
    mouse = pygame.mouse.get_pos()
    current_time = pygame.time.get_ticks()
    if current_time - last_dot_time > dot_interval:
        dot.update_coords((r.randint(0,width),r.randint(0,height)))
        dot.draw(screen)
        last_dot_time = current_time
    #-=-=-=-=-==# Add a random dot
    button0.draw(screen)
    button1.draw(screen)
    button2.draw(screen)
    button3.draw(screen)
    button4.draw(screen)
    print(mouse)
    headin.draw(screen)
    #trailstart
    tr.erasetrail(screen,background)
    tr.updatetrail(mouse)
    tr.drawtrail(screen)
    #trailend
    pygame.display.flip()

    clock.tick(60)


