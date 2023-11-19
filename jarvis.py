
import pygame
import sys
import CLASSES as c
import cosmetics as cm
import CONVEXHULL as ch
import random as r

background = (0,15,15)
eraseline = c.line(1,1,background)
def get_points():
    ps = []
    with open("points.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps
def drawhull(screen,points, hull_points):
        for p in points:
            p.draw(screen)
        for i in range(len(hull_points) - 1):
            points[hull_points[i]].draw_to_point(screen, points[hull_points[i + 1]])
        if len(hull_points) > 1:
            points[hull_points[-1]].draw_to_point(screen, points[hull_points[0]])
            
       
def drawhullfinal(screen,points, hull_points):
        c = (0,200,200)    
        for p in points:
            p.draw(screen)
        for i in range(len(hull_points) - 1):
            points[hull_points[i]].drawcustom(screen, points[hull_points[i + 1]],c)
        if len(hull_points) > 1:
            points[hull_points[-1]].drawcustom(screen, points[hull_points[0]],c)
            
       
        
def jar(screen,points = 0):
    pygame.init()
    clock = pygame.time.Clock()
    
    ppoints = get_points()
    points = []
    pc = (0,150,150)
    for a in ppoints:
        points.append(c.point(a[0],a[1],pc,5)) 
    # jvm
    jarvis_march = ch.JarvisMarch(points)
    leftmost_point = jarvis_march.leftmost_point()
    hull_points_indices = [leftmost_point]
    running = True
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
    once = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
        clock.tick(60)
        drawhull(screen,points, hull_points_indices)
    
        # Incrementally add to hull
        next_point = jarvis_march.next_hull_point(hull_points_indices[-1])
        if next_point == leftmost_point:
            if once == 0:
                screen.fill(background)
                once =1 
            
            drawhullfinal(screen,points, hull_points_indices)  
        else:
            
            hull_points_indices.append(next_point)
            drawhull(screen,points, hull_points_indices)
            pygame.time.wait(500)  # Delay for 2 seconds before drawing the next line
        
        mouse =  pygame.mouse.get_pos()
        print(mouse)
        #=-=-=-shahske
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
