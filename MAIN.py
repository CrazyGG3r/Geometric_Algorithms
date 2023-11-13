import pygame
import sys
import CLASSES as c
import random as r

pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Segment Intersection Demo")

point = c.point(100,300,(233,2,33))
p2 = c.point(600,400,(33,55,66))
l = c.line(2,4,(30 ,30,30))
ps = []
for _ in range(10):
        x = r.randint(0,width-10)
        y = r.randint(0,height-10)
        ps.append(c.point(x, y, (r.randint(0,255),r.randint(0,255),r.randint(0,255))))

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
    #l.draw(screen,point,p2)
    #point.draw(screen)
    #p2.draw(screen)
    #b = p2
    for a in ps:
        for b in ps:
            l.draw(screen,b,a)
    for a in ps:
        a.draw(screen)
    # Update the display
    pygame.display.flip()
