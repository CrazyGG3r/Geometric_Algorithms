from numpy.random import f
import pygame 
import CLASSES as c
import cosmetics as cm
import CONVEXHULL as ch

def get_points():
    ps = []
    with open("points.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps
def conv(screen):
    pygame.init()
    ps = get_points()
    plottablepoints = []
    pc = (0,150,150)
    #convert points in to plottable points
    for a in ps:
        plottablepoints.append(c.point(a[0],a[1],pc,5))
    #
    background = (0,15,15)
    clock = pygame.time.Clock()
    #effects=-=-=-=-=-=--=-=
    #dot
    dot = c.point(0,0,(0,40,40),5)
    dot_interval = 200
    last_dot_time = 0
    #trail
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    #=-=-=-=-=-=-=-=--=-=-=-=
    #buttons
    lbx = 50
    lby = 100
    bw = 200
    bh = 40
    ft = cm.fonts[0]
    tc = (0,150,150)
    size = 36
    b1 = c.Button("Jarvis March",lbx,lby,bw,bh,ft,size,tc,None)
    b2 = c.Button("Graham Scan",lbx,lby+50,bw,bh,ft,size,tc,None)
    butt  = [b1,b2]
    #=-=-=-=-=-=-=-
    screen.fill(background)
    while True:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
         for a in plottablepoints:
             a.draw(screen) 
         for a in butt:
             a.draw(screen)
         pygame.display.flip()