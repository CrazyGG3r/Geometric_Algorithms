from tkinter import W
import pygame
import CLASSES as c
import cosmetics as cm
import random as r

def savetofile(points):
    points_list = points
    with open('points.txt', 'w') as file:
        for point in points_list:
            file.write(f"{point[0]},{point[1]}\n")
            
def drawpoints(screen):
    pygame.init()
    #dot
    dot = c.point(0,0,(0,19,19),100)
    dot_interval = 1000
    last_dot_time = 0
    #trail
    #mouse effects
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-
    background = (0,15,15)
    tc = (0,150,150)
    bpx = 500
    bpy = 600 
    bw = 200
    bh = 40
    onft = cm.fonts[0]
    b1 = c.Button("Done Drawing",bpx,bpy,bw,bh,onft,40,tc,savetofile)
   

    butt = [b1]
    #-0=--=-
    p4 = []
    points = []
    screen.fill(background)
    drawn = False
    running = True
    m= pygame.mouse.get_pos()
    while running:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             
             elif event.type == pygame.MOUSEMOTION:
                 for a in butt:
                     a.is_hovered = a.x < event.pos[0] < a.x + a.width and a.y < event.pos[1] < a.y + a.height
          
             elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                 for a in butt:
                     if a.is_hovered:
                         a.is_clicked = True
          
                 if not drawn:
                     if event.button == 1:
                        m = pygame.mouse.get_pos()
                        points.append(m)
                        p4.append(c.point(m[0],m[1],(0,255,255),5))
                        print("Point SELEECTED!")
          
             elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                 for a in butt:
                     if a.is_clicked and a.is_hovered:
                         a.is_clicked = False
                         if a == b1:
                             drawn = True
                             a.action(points)
                             screen.fill(background)
                             return
                       
          
             if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                 return
           #if drawn == False:
           #    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           #          m = pygame.mouse.get_pos()
           #          points.append(m)
           #          p4.append(c.point(m[0],m[1],(0,255,255),5))
           #          print("Point SELEECTED!")
          mouse = pygame.mouse.get_pos()
          print(mouse)
          #trailstart
          tr.erasetrail(screen,background)
          tr.updatetrail(mouse)
          tr.drawtrail(screen)
          #trailend
          current_time = pygame.time.get_ticks()
          if current_time - last_dot_time > dot_interval:
              dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
              dot.draw(screen)
              last_dot_time = current_time
          for a in p4:
              a.draw(screen)
          for a in butt:
              a.draw(screen)
          pygame.display.flip()
          
          