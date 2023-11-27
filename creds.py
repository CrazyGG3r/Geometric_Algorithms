import pygame
import CLASSES as c
import cosmetics as cm 
import random as r


def color(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
        screen.fill((0,r.randint(0,255),r.randint(0,255)))
        pygame.display.flip()
def creds(screen):
    background = (0,15,15)
    clock = pygame.time.Clock()
    #effects=-=-=-=-=-=--=-=
    fps = round(clock.get_fps(),2)
    fp = str(fps)
    fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
    dframe = c.point(10,700,(0,10,10),70)
    #dot
    lc = (0,25,25)
    line = c.line(2,1,lc)
    aline= c.line(2,1,lc)
    dc = (0,35,35)
    dot = c.point(0,0,dc,5)
    dot_interval = 50
    last_dot_time = 0
    #trail
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-=-=-=-=-=-=--=-=-=-=
    tc = (0,150,150) 
    heading = c.Text("Made by :",cm.fonts[0],40,tc,480,220)
    running = True
    b1x = 290
    b1y = 300
    bw = 240
    bh = 40
    tc = (0,150,150)
    b1 = c.Button("Shaheer Ul Islam"      ,b1x          ,b1y,bw,bh,cm.fonts[0],36,tc,color)    
    b2 = c.Button("Saeed Saleem",b1x + bw + 100,b1y,bw+60,bh,cm.fonts[0],36,tc,color)    
    
    butt = [b1,b2]
    page_requested = None
    screen.fill(background)
    while running:
        dt = clock.tick(60) / 1000.0
        mouse = pygame.mouse.get_pos()
        print(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
            elif event.type == pygame.MOUSEMOTION:  
                for a in butt:           
                    a.is_hovered = a.x < event.pos[0] < a.x + a.width and a.y < event.pos[1] < a.y + a.height
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for a in butt:
                    if a.is_hovered:
                      a.is_clicked = True       
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                for a in butt:
                    if a.is_hovered and a.is_clicked:
                        a.is_clicked = False
                        page_requested = a.action 
                        break
        if page_requested:
            screen.fill(background)  
            page_requested(screen)  
            screen.fill(background)
            page_requested = None
        #dots and lines
        current_time = pygame.time.get_ticks()
        if current_time - last_dot_time > dot_interval:
            dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
            dot.draw(screen)
           
            line.idraw(screen,(r.randint(0,screen.get_width()),r.randint(0,screen.get_height())),(r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
            last_dot_time = current_time
        heading.draw(screen)            


        for a in butt:
            a.draw(screen)
        #frames=-=-=-    
        fm.update_text(str(round(clock.get_fps(),2)))
        dframe.draw(screen)
        fm.draw(screen)  
        #trail
        tr.erasetrail(screen,background)
        tr.updatetrail(mouse)
        tr.drawtrail(screen)
        pygame.display.flip()