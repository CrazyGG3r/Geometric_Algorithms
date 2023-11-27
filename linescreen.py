import pygame 
import CLASSES as c
import cosmetics as cm
import CONVEXHULL as ch
import random as r
import LIINESEC as Lin
import ccw 
import slope as slo
def get_points():
    ps = []
    with open("line.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps

def conv(screen):
    background = (0,15,15)
    ps = get_points()
    plottablepoints = []
    pc = (0,150,150)
    #convert points in to plottable points
    for a in ps:
        plottablepoints.append(c.point(a[0],a[1],pc,5))
    #
    background = (0,15,15)
    clock = pygame.time.Clock()
    linee = c.line(1,2,(0,90,90))
    #effects=-=-=-=-=-=--=-=
    fps = round(clock.get_fps(),2)
    fp = str(fps)
    fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
    dframe = c.point(10,700,(0,10,10),70)
    #dot
    ld = c.line(50,1,(0,10,10))
    dot = c.point(0,0,(0,10,10),60)
    dot_interval = 1000
    last_dot_time = 0
    #trail
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-=-=-=-=-=-=--=-=-=-=
    #buttons
    lbx = 10
    lby = 650
    bw = 200
    bh = 40
    ft = cm.fonts[0]
    tc = (0,150,150)
    size = 25
    off = 50
    ox = bw + 50
    b1 = c.Button("Line Sweep"       ,lbx       ,lby,bw,bh,ft,size,tc,Lin.lineint)
    b2 = c.Button("CCW"              ,lbx+(ox*1),lby,bw,bh,ft,size,tc,ccw.cw)
    b3 = c.Button("Slope",lbx+(ox*2),lby,bw,bh,ft,size,tc,slo.slop)
    screen.fill(background)
    butt  = [b1,b2,b3]
    page_requested = None
    
    while True:
         mouse = pygame.mouse.get_pos() 
         dt = clock.tick(60) / 1000.0
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
             ld.idraw(screen,(r.randint(0,screen.get_width()),r.randint(0,screen.get_height())),(r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
             last_dot_time = current_time
         linee.update(dt)
         fm.update_text(str(round(clock.get_fps(),2)))
         dframe.draw(screen)
         fm.draw(screen)  
         linee.draw(screen,plottablepoints[0],plottablepoints[1])
         linee.draw(screen,plottablepoints[2],plottablepoints[3])
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