import pygame
import sys
import CLASSES as c


pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Segment Intersection Demo")

point = c.point(100,300,(233,2,33))
p2 = c.point(600,400,(33,55,66))
l = c.line(1,10,(220,220,100))

clock = pygame.time.Clock()
# Main game loop
while True:
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # Draw line segments
    
    l.update(dt)
    l.draw(screen,point,p2)
    point.draw(screen)
    p2.draw(screen)
    # Update the display
    pygame.display.flip()
