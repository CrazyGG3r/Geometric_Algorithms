from pickle import FALSE
import pygame
import sys
import CLASSES as c
import random as r
import CONVEXHULL as cv 
pygame.init()

# Set up the window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line Segment Intersection Demo")

point = c.point(100,300,(233,2,33))
p2 = c.point(600,400,(33,55,66))
ldur = 1
l = c.line(2,ldur,(200 ,200,30))
ps = []
for _ in range(10):
        x = r.randint(0,width-10)
        y = r.randint(0,height-10)
        ps.append(c.point(x, y, (r.randint(0,255),r.randint(0,255),r.randint(0,255))))


for a in range(0,len(ps)):
    print("(",ps[a].x,",",ps[a].y,")")
jarvis_march = cv.JarvisMarch(ps)
cvh = jarvis_march.convex_hull()
print(type(cvh[0]))

clock = pygame.time.Clock()
# Main game loop
i = 0
curr = cvh[i+1]
prev = cvh[i]
space = False
while True:
     
    dt = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space = True
    if space == False:
        continue
    
    for a in ps:
        a.draw(screen)
        
    l.update(dt)
    if l.elapsed != ldur:
        l.draw(screen,prev,curr)
    else:
        if i == len(cvh)-1:
            curr = cvh[0]
            prev = cvh[-1]
        else:
            prev = curr
            curr = cvh[i+1]
            i = i+1
        l.elapsed = 0
        l.draw(screen,prev,curr)
    for a in ps:
        a.draw(screen)
    # Update the display
    pygame.display.flip()

