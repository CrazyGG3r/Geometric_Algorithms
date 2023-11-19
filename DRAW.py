
import pygame
import CLASSES as c
import cosmetics as cm
import random as r
def savetofilel(points):
    points_list = points
    with open('line.txt', 'w') as file:
        for point in points_list:
            file.write(f"{point[0]},{point[1]}\n")
def savetofile(points):
    points_list = points
    with open('points.txt', 'w') as file:
        for point in points_list:
            file.write(f"{point[0]},{point[1]}\n")
def drawline(screen): 
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

    
    p4 = []
    points = []
    screen.fill(background)
    running = True
    m= pygame.mouse.get_pos()
    clock = pygame.time.Clock()
    selected = 0
  
    while running:
          for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
                 
             elif event.type == pygame.MOUSEBUTTONUP and event.button== 1:
                if selected <= 4:
                    m = pygame.mouse.get_pos()
                    points.append(m)
                    p4.append(c.point(m[0],m[1],(0,255,255),5))
                    selected +=1
                    print("something SELEECTED!")
                if selected == 5:
                   
                    points.pop()
                    savetofilel(points)
                    return
             if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                 return
          current_time = pygame.time.get_ticks()
          if current_time - last_dot_time > dot_interval:
              dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
              dot.draw(screen)
              last_dot_time = current_time
          for a in p4:
              a.draw(screen)
          if len(p4)%2==0 and len(p4)%4 != 0 and len(p4)!=0 :
              a1 = p4[0]
              a2 = p4[1]
              a1.draw_to_point(screen,a2)
              
          if len(p4)%4 == 0 and len(p4) != 0 :
              a1 = p4[0]
              a2 = p4[1]
              a1.draw_to_point(screen,a2)
              a3 = p4[2]
              a4 = p4[3]
              a3.draw_to_point(screen,a4)
          mouse = pygame.mouse.get_pos()
          print(mouse)
          #trailstart
          tr.erasetrail(screen,background)
          tr.updatetrail(mouse)
          tr.drawtrail(screen)
          #trailend
          clock.tick(60)
          pygame.display.flip()
    
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
    clock = pygame.time.Clock()
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
          
          
             elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                 for a in butt:
                     if a.is_clicked and a.is_hovered:
                         a.is_clicked = False
                         if a == b1:
                             drawn = True
                             a.action(points)
                             screen.fill(background)
                             return
                       
                 if not drawn:
                     if event.button == 1:
                        m = pygame.mouse.get_pos()
                        points.append(m)
                        p4.append(c.point(m[0],m[1],(0,255,255),5))
                        print("Point SELEECTED!")
          
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
          clock.tick(60)
          pygame.display.flip()
          
          