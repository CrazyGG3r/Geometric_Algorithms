from asyncio.windows_events import NULL
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
background =(0,23,23)



#mouse effects
firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
tr = c.trail(firstset,7)

#menu text
hcolor = (0,158,158)
headin = c.Text("Geometric Algorithms",cm.fonts[0],50,hcolor,320,90)
dot = c.point(0,0,(0,90,90),5)
dot_interval = 500
last_dot_time = 0
l = c.line(1,10,(50,50,50))
screen.fill(background)


#buttons
def dummdumm(screen = NULL):
    print("dumdum")
b1 = 535
b2 = 150
buttoncolor = (0,170,170)
button1 = c.Button("Jarvis March",b1,b2   ,150,40,cm.fonts[0],20,buttoncolor,dummdumm)
button2 = c.Button("Quick Hull"  ,b1,b2+30,150,40,cm.fonts[0],20,buttoncolor,dummdumm)
while running:
      
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Check if the mouse is over the button
            button1.is_hovered = button1.x < event.pos[0] < button1.x + button1.width and \
            button1.y < event.pos[1] < button1.y + button1.height
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the left mouse button is clicked
            if button1.is_hovered:
                button1.is_clicked = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Check if the left mouse button is released
            if button1.is_clicked:
                button1.is_clicked = False
                button1.action()        
    current_time = pygame.time.get_ticks()
    
    button1.draw(screen)
    if current_time - last_dot_time > dot_interval:
        dot.update_coords((r.randint(0,width),r.randint(0,height)))
        dot.draw(screen)
        last_dot_time = current_time
        # Add a random dot
    mouse = pygame.mouse.get_pos()
    print(mouse)
    headin.draw(screen)
    
    #trailstart
    tr.erasetrail(screen,background)
    tr.updatetrail(mouse)
    tr.drawtrail(screen)
    #trailend
    pygame.display.flip()

    clock.tick(60)


