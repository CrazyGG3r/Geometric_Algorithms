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
def conv():
    pygame.init()
    ps = get_points()
    plottablepoints = []
    pc = (0,150,150)
    #convert points in to plottable points
    for a in ps:
        plottablepoints.append(c.point(a[0],a[1],))
    #

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
    
    
    