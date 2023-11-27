import pygame
import sys
import random
from cosmetics import fonts
from CLASSES import point as Point
# Initialize Pygame
def do_segments_intersect(segment1, segment2):
    #x1, y1, x2, y2 = segment1
    #x3, y3, x4, y4 = segment2
    
    # Extract the coordinates from the Point objects
    x1, y1 = segment1[0].x, segment1[0].y
    x2, y2 = segment1[1].x, segment1[1].y
    x3, y3 = segment2[0].x, segment2[0].y
    x4, y4 = segment2[1].x, segment2[1].y
    # Check for vertical lines
    if x1 == x2:
        m1 = float('inf')
    else:
        m1 = (y2 - y1) / (x2 - x1)

    if x3 == x4:
        m2 = float('inf')
    else:
        m2 = (y4 - y3) / (x4 - x3)

    # Check for parallel lines
    if m1 == m2:
        return False, None

    # Calculate intersection point
    x_int = (y3 - y1 + m1 * x1 - m2 * x3) / (m1 - m2)
    y_int = m1 * (x_int - x1) + y1

    # Check if intersection point is within the segments
    if (
        min(x1, x2) <= x_int <= max(x1, x2)
        and min(x3, x4) <= x_int <= max(x3, x4)
        and min(y1, y2) <= y_int <= max(y1, y2)
        and min(y3, y4) <= y_int <= max(y3, y4)
    ):
        return True, (int(x_int), int(y_int))
    else:
        return False, None
def get_line_segments():
    pc = (0,150,150)
    with open("line.txt", 'r') as file:
        lines = file.readlines()
        points = [tuple(map(int, line.strip().split(','))) for line in lines]
        segment1 = (Point(points[0][0], points[0][1],pc,5), Point(points[1][0], points[1][1],pc,5))
        segment2 = (Point(points[2][0], points[2][1],pc,5), Point(points[3][0], points[3][1],pc,5))
        return segment1, segment2  # Make sure to return the segments


def slop(scr):
    global screen 
    screen = scr
    pygame.init()
    global segment1
    global segment2 
    segments = get_line_segments()
    segment1 = segments[0]
    segment2 = segments[1]
    
    # Constants
    WIDTH, HEIGHT = screen.get_width(),screen.get_height()
    WHITE = (0,15,15)
    RED = (0,150,150)
    GREEN = (40 , 255, 100)
    # Function to check if two line segments intersect
    
    
    # Set up the screen
    
    
    # Check if the segments intersect
    intersection, intersection_point = do_segments_intersect(segment1, segment2)
    
    # Draw the line segments
    
    screen.fill(WHITE)
    pygame.draw.line(screen, RED, (segment1[0].x, segment1[0].y), (segment1[1].x, segment1[1].y), 2)
    pygame.draw.line(screen, RED, (segment2[0].x, segment2[0].y), (segment2[1].x, segment2[1].y), 2)
    # Display gradients
    font = pygame.font.Font(fonts[0], 20)
    
    if segment1[0] != segment1[1]:
        gradient1 = round((segment1[1].y - segment1[0].y) / (segment1[0].x - segment1[1].x), 2)
    else:
        gradient1 = "Vertical"
    
    if segment2[0] != segment2[1]:
        gradient2 = round((segment2[1].y - segment2[0].y) / (segment2[0].x - segment2[1].x), 2)
    else:
        gradient2 = "Vertical"
    
    text1 = font.render(f"Gradient 1: {gradient1}", True, RED)
    text2 = font.render(f"Gradient 2: {gradient2}", True, RED)
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 50))
    
    # Draw the intersection point if there is an intersection
    if intersection:
        pygame.draw.circle(screen, GREEN, intersection_point, 5)
        text3 = font.render("The segments intersect!", True, GREEN)
        # Extend the lines to show intersection
       
    else:
            text3 = font.render("The segments do not intersect.", True, RED)
    seg = [segment1,segment2]
    for a in seg:
        a[0].draw(screen)
        a[1].draw(screen)

    screen.blit(text3, (10, 90))
    
    
    # Update the display
    pygame.display.flip()
    
    # Main loop to handle events
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return
