from turtle import Screen
import pygame
import sys
import random
import time
from CLASSES  import point as Point, Text
import cosmetics as cm
def onSegment(p, q, r):
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
            q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False

def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def doIntersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if (o1 == 0 and onSegment(p1, p2, q1)) or \
       (o2 == 0 and onSegment(p1, q2, q1)) or \
       (o3 == 0 and onSegment(p2, p1, q2)) or \
       (o4 == 0 and onSegment(p2, q1, q2)):
        return True

    return False

def draw_line(screen, color, start, end):
    pygame.draw.line(screen, color, (start.x, start.y), (end.x, end.y), 2)


def draw_point(screen, color, point):
    pygame.draw.circle(screen, color, (point.x, point.y), 5)




def get_line_segments():
    pc = (0,200,200)
    
    with open("line.txt", 'r') as file:
        lines = file.readlines()
        points = [tuple(map(int, line.strip().split(','))) for line in lines]
        # Make sure your file has exactly four lines, each containing an x,y pair
        segment1 = (Point(points[0][0], points[0][1],pc,5), Point(points[1][0], points[1][1],pc,5))
        segment2 = (Point(points[2][0], points[2][1],pc,5), Point(points[3][0], points[3][1],pc,5))
        return segment1, segment2

def cw(scr):
    global screen
    screen = scr
    segments = get_line_segments()
    segment1, segment2 = segments
    segment1_start, segment1_end = segment1
    segment2_start, segment2_end = segment2
    
    
    
    # Check if the line segments intersect
    intersection = doIntersect(segment1_start, segment1_end, segment2_start, segment2_end)
    
    # Display the result of the intersection check
    f = Text("Intersect" if intersection else "No Intersect",cm.fonts[0],36,(0,150,150),10,10)
    f.draw(screen)
    ox = 10
    oy = 50
    oo= 40
    # Display the orientation of the line segments
    orientation1 = Text("o1: " +str(orientation(segment1_start, segment1_end, segment2_start)),cm.fonts[0],26,(0,145,145),ox,oy)
    orientation2 = Text("o2: " +str(orientation(segment1_start, segment1_end, segment2_end  )),cm.fonts[0],26,(0,145,145),ox,oy +( oo*1))
    orientation3 = Text("o3: " +str(orientation(segment2_start, segment2_end, segment1_start)),cm.fonts[0],26,(0,145,145),ox,oy +( oo*2))
    orientation4 = Text("o4: " +str(orientation(segment2_start, segment2_end, segment1_end  )),cm.fonts[0],26,(0,145,145),ox,oy +( oo*3))
    
    ore = [orientation1,orientation2,orientation3,orientation4]
    
    
    # Update the display
    pygame.display.flip()
    background = (0,15,15)
    # Delay before starting to draw lines
    time.sleep(1)
    fc = (0,150,150)
    lc = (0,130,130)
    pc = (0,200,200)
    
    clock = pygame.time.Clock()
    # Main loop to handle events and draw lines gradually
    running = True
    progress = 0
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 15, 15))  # Background color

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
               return

        # Increment progress for line drawing
        progress += 0.01
        if progress >= 1.0:
            progress = 1.0

        # Calculate intermediate points
        intermediate_point1 = Point(
            int(segment1_start.x + progress * (segment1_end.x - segment1_start.x)),
            int(segment1_start.y + progress * (segment1_end.y - segment1_start.y)),
            pc, 5
        )
        intermediate_point2 = Point(
            int(segment2_start.x + progress * (segment2_end.x - segment2_start.x)),
            int(segment2_start.y + progress * (segment2_end.y - segment2_start.y)),
            pc, 5
        )

        # Draw the lines and points
        draw_line(screen, lc, segment1_start, intermediate_point1)
        draw_line(screen, lc, segment2_start, intermediate_point2)
        draw_point(screen, pc, segment1_start)
        draw_point(screen, pc, intermediate_point1)
        draw_point(screen, pc, segment2_start)
        draw_point(screen, pc, intermediate_point2)

        # Draw orientations and intersection result
        for text_object in ore:
            text_object.draw(screen)
        f.draw(screen)

        # Update the display
        pygame.display.flip()

        # Control the drawing speed
        clock.tick(60)

        # Exit the loop after the animation is complete
        if progress >= 1.0:
            running = False

        time.sleep(0.1)  # Small delay to see the animation progressing

# Call the function with the Pygame screen

        
        
        
