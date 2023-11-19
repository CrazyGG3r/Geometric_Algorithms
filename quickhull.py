import pygame
import sys
import CLASSES as c
import cosmetics as cm
import CONVEXHULL as ch
import random as r
def get_points():
    ps = []
    with open("points.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps

def qui(screen):
    clock = pygame.time.Clock()
    pygame.init()
    background = (0,15,15)
    ppoints = get_points()
    points = []
    pc = (0,150,150)
    for a in ppoints:
        points.append(c.point(a[0],a[1],pc,5))

    #effects=-=-=-=-=-=--=-=
    fps = round(clock.get_fps(),2)
    fp = str(fps)
    fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
    dframe = c.point(10,700,(0,10,10),70)
    #dot=-=-=
    dot = c.point(0,0,(0,10,10),60)
    dot_interval = 3000
    last_dot_time = 0
    #trail-=-=-
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-=-=-=-=-=-=--=-=-=-=
    screen.fill(background)
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
        mouse =  pygame.mouse.get_pos()
        print(mouse)
        #graham here

        #shashke =-=-=-=-=
        fm.update_text(str(round(clock.get_fps(),2)))
        dframe.draw(screen)
        fm.draw(screen)   
        current_time = pygame.time.get_ticks()
        if current_time - last_dot_time > dot_interval:
            dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
            dot.draw(screen)
            last_dot_time = current_time
        for a in points:
            a.draw(screen)
        #trailstart
        tr.erasetrail(screen,background)
        tr.updatetrail(mouse)
        tr.drawtrail(screen)
        #trailend    
        pygame.display.flip()
        clock.tick(60)
