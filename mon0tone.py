from turtle import Screen
import pygame
import random
import sys
from CLASSES import point as Point

pygame.init()
clock = pygame.time.Clock()
def get_points():
    ps = []
    with open("points.txt", 'r') as file:
            for line in file:
                coordinates = line.split(',')
                x, y = map(int, coordinates)
                ps.append((x, y)) 
    return ps



def draw(points, upper_hull, lower_hull, current_point):
    screen.fill((0, 15,15))  # Clear screen
    # Draw all points
    for p in points:
        p.draw(screen)
    # Draw upper hull lines (in blue)
    for i in range(len(upper_hull) - 1):
        upper_hull[i].draw_to_point(screen, upper_hull[i + 1], (255, 162, 3))
    # Draw lower hull lines (in green)
    for i in range(len(lower_hull) - 1):
        lower_hull[i].draw_to_point(screen, lower_hull[i + 1], (3, 255, 108))
    # Draw current point
    current_point.draw(screen)
    pygame.display.flip()

# Create random points
    

# Sort points by x-coordinate

# Initialize Monotone Chain Convex Hull
global upper_hull
global lower_hull
def momo(scr):
    global screen
    upper_hull = []
    lower_hull = []
    screen = scr
    ps = get_points()
    global points
    points = []
    global pc
    pc = (0,150,150)
    for a in ps:
        points.append(Point(a[0],a[1],pc,5))    
    sorted_points = sorted(points, key=lambda p: (p.x, p.y))
    # Main loop
    running = True
    current_point_index = 0
    
    while running:
        for event in pygame.event.get(  ):
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
        # Update and draw
        draw(sorted_points, upper_hull, lower_hull, sorted_points[current_point_index])
        
        # Adjust the frame rate as needed
        clock.tick(1)  # 5 frames per second
    
        # Build upper hull
        while len(upper_hull) >= 2 and (upper_hull[-1].x - upper_hull[-2].x) * (sorted_points[current_point_index].y - upper_hull[-2].y) - (upper_hull[-1].y - upper_hull[-2].y) * (sorted_points[current_point_index].x - upper_hull[-2].x) > 0:
            upper_hull.pop()
    
        upper_hull.append(sorted_points[current_point_index])
        
        # Build lower hull
        while len(lower_hull) >= 2 and (lower_hull[-1].x - lower_hull[-2].x) * (sorted_points[current_point_index].y - lower_hull[-2].y) - (lower_hull[-1].y - lower_hull[-2].y) * (sorted_points[current_point_index].x - lower_hull[-2].x) < 0:
            lower_hull.pop()
    
        lower_hull.append(sorted_points[current_point_index])
    
        current_point_index += 1
    
        if current_point_index >= len(sorted_points):
            # Draw the final hull
            draw(sorted_points, upper_hull, lower_hull, Point(0, 0, (0, 200, 200),5))
    
            # Wait for 2 seconds before quitting
            clock.tick(1)
            running = False
    lower_hull = []
    upper_hull = []
    return 

