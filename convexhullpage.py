import pygame
import random as r
import CLASSES as c
import sys
import CONVEXHULL as cv
pygame.init()
def check(screen):
    return
def conv(screen):
    screen.fill((0,10,10))
    pygame.init()
    #SETUP AND POINT GENERATE
    psize = 5
    ldur = 1
    l = c.line(2,ldur,(0 ,60,60))
    ps = []
    for _ in range(10):
        x = r.randint(0,screen.get_width()-10)
        y = r.randint(0,screen.get_height()-10) 
        ps.append(c.point(x, y, (0,150,150),psize))
    jarvis_march = cv.JarvisMarch(ps)
    cvh = jarvis_march.convex_hull()
    clock = pygame.time.Clock()
    # Main game loop
    i = 0
    curr = cvh[i+1]
    prev = cvh[i]
    space = False
    screen.fill((0,10,10)) 
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
        print("1")