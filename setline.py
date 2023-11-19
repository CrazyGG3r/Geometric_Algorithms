import pygame
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import CLASSES as c
import cosmetics as cm
import random as r
import DRAW

def file_selected(file_path):
    file_name_without_extension, _ = os.path.splitext(os.path.basename(file_path))
    return file_name_without_extension
def select_file(screen  = None):
    root = tk.Tk()
    root.withdraw()  
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        copy_file_to_program_directory(file_path)
        print("UPLOADED!")
        f = file_selected(file_path) +".txt"
        
        return f
    else:
        return 
def copy_file_to_program_directory(file_path):
    destination = os.path.join('', "points.txt")  
    shutil.copy(file_path, destination)
    print(f"Copied file to {destination}")

    shutil.copy(file_path, destination)
    print(f"Copied file to {destination}")
  
def randomizetenpoints(sc = None):
    x = 0
    y = 0
    p =[]
    for _ in range(0,10):
        x = r.randint(320,640)
        y = r.randint(180,360)
        p.append((x,y))
    with open('points.txt', 'w') as file:
        for point in p:
            file.write(f"{point[0]},{point[1]}\n")
def randomizefourpoints(sc = None):
    x = 0
    y = 0
    p =[]
    for _ in range(0,4):
        x = r.randint(320,640)
        y = r.randint(180,360)
        p.append((x,y))
    with open('line.txt', 'w') as file:
        for point in p:
            file.write(f"{point[0]},{point[1]}\n")
pygame.init()

running = True
def setline(screen):
    #dot
    dot = c.point(0,0,(0,40,40),5)
    dot_interval = 200
    last_dot_time = 0
    #trail
    #mouse effects
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-
    tc = (0,150,150)
    
    b1px = 450
    b1py = 200
    bw = 260
    bh = 40
    onft = cm.fonts[0]
    b1 = c.Button("Draw line",b1px,b1py,bw,bh,onft,36,tc,DRAW.drawline)
    
    b2 = c.Button("Randomize Line",b1px,b1py+50,bw,bh,onft,36,tc,randomizefourpoints)
    clock = pygame.time.Clock()
    background = ((0,15,15))
    screen.fill(background)
    pygame.init()
    butt = [b1,b2]
    running = True
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
                        screen.fill(background)
                        f = a.action(screen) 
                        screen.fill(background)
                        break
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
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
        for a in butt:
            a.draw(screen)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    