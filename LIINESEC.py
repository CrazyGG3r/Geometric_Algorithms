
import pygame
import sys
import random
import time
import CLASSES as c
import cosmetics as cm
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Function to check if two line segments intersect
def do_segments_intersect(segment1, segment2):
    p1, q1 = segment1
    p2, q2 = segment2

    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False

def on_segment(p, q, r):
    return min(p.x, r.x) <= q.x <= max(p.x, r.x) and min(p.y, r.y) <= q.y <= max(p.y, r.y)


def draw_line(screen, color, start, end):
    pygame.draw.line(screen, color, (start.x, start.y), (end.x, end.y), 2)


def draw_point(screen, color, point):
    pygame.draw.circle(screen, color, (point.x, point.y), 5)
def get_line_segments():
    with open("line.txt", 'r') as file:
        lines = file.readlines()
        points = [tuple(map(int, line.strip().split(','))) for line in lines]
        segment1 = (Point(points[0][0], points[0][1]), Point(points[1][0], points[1][1]))
        segment2 = (Point(points[2][0], points[2][1]), Point(points[3][0], points[3][1]))
        return segment1, segment2  # Make sure to return the segments


def lineint(scr):
    global screen
    screen = scr
    HEIGHT = screen.get_height()
    WIDTH = screen.get_width()
    segments = get_line_segments()
    segment1 = segments[0]
    segment2 = segments[1]
    background = (0,15,15)
    
    
    # Main loop to handle events
    for i in range(101):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # Draw the lines gradually
        progress = i / 100.0
        intermediate_point1 = Point(int(segment1[0].x + progress * (segment1[1].x - segment1[0].x)),
                                    int(segment1[0].y + progress * (segment1[1].y - segment1[0].y)))
        intermediate_point2 = Point(int(segment2[0].x + progress * (segment2[1].x - segment2[0].x)),
                                    int(segment2[0].y + progress * (segment2[1].y - segment2[0].y)))
        
        # Draw the line segments and points
        screen.fill(background)
        lc = (0,30,30)
        pc = (0,160,160)
        draw_line(screen, lc, segment1[0], intermediate_point1)
        draw_line(screen, lc, segment2[0], intermediate_point2)
        draw_point(screen, pc, segment1[0])
        draw_point(screen,pc, intermediate_point1)
        draw_point(screen, pc, segment2[0])
        draw_point(screen, pc, intermediate_point2)
        
        # Draw the sweep lines
        pygame.draw.line(screen, (0,255,255), (WIDTH * progress, 0), (WIDTH * progress, HEIGHT), 2)
    
        # Update the display
        pygame.display.flip()
    
        # Introduce a small delay to control the drawing speed
        pygame.time.delay(20)
        colo = (0,50,50)
    pygame.draw.line(screen, colo, (segment1[0].x, 0), (segment1[0].x, HEIGHT), 2)
    pygame.draw.line(screen, colo, (segment1[1].x, 0), (segment1[1].x, HEIGHT), 2)
    pygame.draw.line(screen, colo, (segment2[0].x, 0), (segment2[0].x, HEIGHT), 2)
    pygame.draw.line(screen, colo, (segment2[1].x, 0), (segment2[1].x, HEIGHT), 2)
    pygame.time.delay(500)
    
    intersection = do_segments_intersect(segment1, segment2)
    
    # Display the result of the intersection check
    fc = (0,200,200)
    font = pygame.font.Font(None, 36)
    text = c.Text("Lines Intersect!" if intersection else "Lines Donot Intersect!",cm.fonts[0],36,fc,100,100)
    text.draw(screen)
    # Update the display
    pygame.display.flip()



    # Main loop to handle events after the lines are drawn
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
