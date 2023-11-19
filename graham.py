import pygame
import sys
import random
import math
from functools import cmp_to_key
import CLASSES as c
import cosmetics as cm
import random as r
# Assuming CLASSES.py contains the classes point, Text, and trail
from CLASSES import point, Text, trail
# Assuming CONVEXHULL.py contains the GrahamScanVisualization class
class GrahamScanVisualization:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # Collinear
        elif val > 0:
            return 1  # Clockwise
        return 2  # Counterclockwise

    def graham_scan(self):
        n = len(self.points)
        if n < 3:
            return []

        pivot = min(self.points, key=lambda p: (p.y, p.x))
        sorted_points = sorted(self.points, key=lambda p: math.atan2(p.y - pivot.y, p.x - pivot.x))
        self.hull = [pivot, sorted_points[0], sorted_points[1]]

        for i in range(2, n):
            while len(self.hull) > 1 and self.orientation(self.hull[-2], self.hull[-1], sorted_points[i]) != 2:
                self.draw(sorted_points[i])
                pygame.display.flip()
                clock.tick(60)  # Adjust the frame rate as needed
                self.hull.pop()

            self.hull.append(sorted_points[i])
            self.draw(sorted_points[i])
            pygame.display.flip()
            clock.tick(60)  # Adjust the frame rate as needed

    def draw(self, current_point, accepted=True):
        screen.fill((0,15,15))

        for i in range(len(self.hull) - 1):
            self.hull[i].draw_to_point(screen, self.hull[i + 1])
        if len(self.hull) > 1:
            self.hull[-1].draw_to_point(screen, self.hull[0])

        for p in self.points:
            p.draw(screen)

        # Draw a dotted line to the rejected points
        if not accepted:
            for point in self.points:
                if point not in self.hull:
                    pygame.draw.line(screen, (255, 0, 0), (current_point.x, current_point.y),
                                     (point.x, point.y), 2)

        pygame.display.flip()
        clock.tick(2)  # Adjust the frame rate as needed


# Function to read points from a file
def get_points():
    ps = []
    with open("points.txt", 'r') as file:
        for line in file:
            coordinates = line.split(',')
            x, y = map(int, coordinates)
            ps.append((x, y))
    return ps

# Initialize Pygame and the clock
def gra(scr):
    global screen 
    screen = scr
    global clock
    clock = pygame.time.Clock()
    background = (0,15,15)
    #effects=-=-=-=-=-=--=-=
    fps = round(clock.get_fps(),2)
    fp = str(fps)
    fm = c.Text(fp,cm.fonts[0],12,(0,50,50),10,700)
    dframe = c.point(10,700,(0,10,10),70)
    #dot=-=-=
    dot = c.point(0,0,(0,10,10),60)
    dot_interval = 3000
    last_dot_time = 0
    #trail-=-=-
    firstset = [(0,0),(0,0),(0,0),(0,0),(0,0)]
    tr = c.trail(firstset,7)
    # Function to draw the current state of the Graham Scan
    def draw(points, hull_points, screen):
        screen.fill(background)  # Dark background
    
        # Draw all points
        for p in points:
            p.draw(screen)
            if hull_points != None:
                pygame.draw.lines(screen, (0, 255, 0), True, [(p.x, p.y) for p in hull_points] + [hull_points[0]], 2)
            else:
                pass
        pygame.display.flip()
    
    # Convert points from tuples to point instances
    ppoints = get_points()
    points = [point(x, y, (0, 150, 150), 5) for x, y in ppoints]
    
    # Initialize Graham Scan Visualization
    graham_scan_visualization = GrahamScanVisualization(points)
    
    # Perform the Graham Scan
    hull_points = graham_scan_visualization.graham_scan()
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
        # Draw the current state of the Graham Scan
        draw(points, hull_points, screen)
        clock.tick(60)  # Maintain 60 frames per second
        mouse =  pygame.mouse.get_pos()
        print(mouse)
        #=-=-=-shahske
        fm.update_text(str(round(clock.get_fps(),2)))
        dframe.draw(screen)
        fm.draw(screen)   
        current_time = pygame.time.get_ticks()
        if current_time - last_dot_time > dot_interval:
            dot.update_coords((r.randint(0,screen.get_width()),r.randint(0,screen.get_height())))
            dot.draw(screen)
            last_dot_time = current_time
        for a in points:
              a.draw(screen)
        draw(points,hull_points,screen)
        #trailstart
        tr.erasetrail(screen,background)
        tr.updatetrail(mouse)
        tr.drawtrail(screen)
        #trailend    
    pygame.quit()
    sys.exit()
    