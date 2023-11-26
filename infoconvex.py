import pygame
import CLASSES as c
import cosmetics as cm 
import random as r
def get_points():
    ps = []
    with open("ipoints.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps
def get_pointsr():
    ps = []
    with open("cvh.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps

def cvwhat(screen):
    background = (0,15,15)
    clock = pygame.time.Clock()
    h = get_pointsr()
    plottablehull = []
    pc = (0,150,150)
    #convert points in to plottable points
    for a in h:
        plottablehull.append(c.point(a[0],a[1],pc,5))
    #
    #-=-=-=-=-
    ps = get_points()
    plottablepoints = []
    pc = (0,150,150)
    #convert points in to plottable points
    for a in ps:
        plottablepoints.append(c.point(a[0],a[1],pc,5))
    #
    #effects=-=-=-=-=-=--=-=
    fps = round(clock.get_fps(),2)
    fp = str(fps)
    fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
    dframe = c.point(10,700,(0,10,10),70)
    #dot
    lc = (0,25,25)
    line = c.line(2,1,lc)
    aline= c.line(2,1,lc)
    dc = (0,10,10)
    dot = c.point(0,0,dc,50)
    dot_interval = 1000
    last_dot_time = 0
    #trail
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-=-=-=-=-=-=--=-=-=-=
    tc = (0,150,150) 
    heading = c.Text("What is a: ",cm.fonts[0],40,tc,480,220)
    running = True
    b1x = 290
    b1y = 300
    bw = 240
    bh = 40
    tc = (0,150,150)
    
    
    butt = []
    page_requested = None
    screen.fill(background)
    running = True
    while running: 
         mouse = pygame.mouse.get_pos() 
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
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
                    if a.is_hovered and a.is_clicked:
                        a.is_clicked = False
                        page_requested = a.action
                        break
         if page_requested:
            screen.fill(background)  # Clear the screen before changing the page
            page_requested(screen)  # Call the action associated with the button
            screen.fill(background)
            page_requested = None  # Reset the flag
         current_time = pygame.time.get_ticks()
         if current_time - last_dot_time > dot_interval:
             dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
             dot.draw(screen)
             last_dot_time = current_time
            
         fm.update_text(str(round(clock.get_fps(),2)))
         dframe.draw(screen)
         fm.draw(screen)
         b = plottablehull[0]
         for a in plottablehull:
             a.draw_to_point(screen,b)
             b = a
         b.draw_to_point(screen,plottablehull[0])
         for a in plottablepoints:
             a.draw(screen) 
         for a in butt:
             a.draw(screen)
         clock.tick(60)
         #trailstart
         tr.erasetrail(screen,background)
         tr.updatetrail(mouse)
         tr.drawtrail(screen)
         #trailend
         pygame.display.flip()