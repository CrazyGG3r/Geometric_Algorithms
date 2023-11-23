
import pygame
import sys
import random
import math
from CLASSES import point as Point


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else -1  # Clockwise or counterclockwise

def bruteforce(points):
    n = len(points)
    if n < 3:
        return points

    pivot = min(points, key=lambda p: (p.y, p.x))
    sorted_points = sorted(points, key=lambda p: math.atan2(p.y - pivot.y, p.x - pivot.x))
    convex_hull = [pivot, sorted_points[0], sorted_points[1]]

    for i in range(2, n):
        while len(convex_hull) > 1 and orientation(convex_hull[-2], convex_hull[-1], sorted_points[i]) != -1:
            convex_hull.pop()
        convex_hull.append(sorted_points[i])

    return convex_hull



def draw(points,hull, current_pair):
    start=False
    end=False
    # Draw all points
    for p in points:
        p.draw(screen)

    for i in range(1,len(hull)):
        if hull[i-1].x == current_pair[0].x and hull[i-1].y == current_pair[0].y:
            start=True
            if hull[i].x == current_pair[1].x and hull[i].y == current_pair[1].y:
                end=True
        elif hull[i-1].x == current_pair[1].x and hull[i-1].y == current_pair[1].y:
            start=True
            if hull[i].x == current_pair[0].x and hull[i].y == current_pair[0].y:
                end=True
    
    if current_pair and start==True and end==True:
        pygame.draw.line(screen, (0,255,255), (current_pair[0].x, current_pair[0].y), (current_pair[1].x, current_pair[1].y), 2)
    else:
        pygame.draw.line(screen, (0,100,100), (current_pair[0].x, current_pair[0].y), (current_pair[1].x, current_pair[1].y), 2)
    pygame.draw.line(screen, (0,255,255), (hull[-1].x, hull[-1].y), (hull[0].x, hull[0].y), 2)
    pygame.display.flip()

def final(hull,points):
    screen.fill((0, 15,15))  
  
    for p in points:
        p.draw(screen)
    for i in range(1, len(hull)):
        pygame.draw.line(screen, (0,255,255), (hull[i-1].x, hull[i-1].y), (hull[i].x, hull[i].y), 2)
    pygame.draw.line(screen, (0,255,255), (hull[-1].x, hull[-1].y), (hull[0].x, hull[0].y), 2)  # Connect last point to the first
    pygame.display.flip()
def get_points():
    ps = []
    with open("points.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps

def bruf(scr):
    global screen
    screen = scr
    global clock
    clock = pygame.time.Clock()
    p = get_points()
    points = []
    pc = (0,200,200)
    for a in p:
        points.append(Point(a[0],a[1],pc,5))
    
    
    convex_hull = bruteforce(points)
    
    # Main loop
    running = True
    current_pair = None
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            current_pair = (points[i], points[j])
            draw(points,convex_hull, current_pair)
            clock.tick(10)  # Adjust the frame rate as needed
     
    final(convex_hull,points)
    # Wait for a key press before quitting
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
                
