def conv():
    #SETUP AND POINT GENERATE
    point = c.point(100,300,(233,2,33))
    p2 = c.point(600,400,(33,55,66))
    ldur = 1
    l = c.line(2,ldur,(200 ,200,30))
    ps = []
    for _ in range(10):
        x = r.randint(0,width-10)
        y = r.randint(0,height-10) 
        ps.append(c.point(x, y, (r.randint(0,255),r.randint(0,255),r.randint(0,255))))
    
    #TAKING INPUT
    choice = int(input("Press 1 for Jarvis March\nPress 2 for Graham Scan\nPress 3 for Quick Elimination\n"))
    
    #CONVEX HULLS
    if choice == 1:
        pygame.display.set_caption("Line Segment Intersection Demo")
        screen = pygame.display.set_mode((width, height))
        jarvis_march = cv.JarvisMarch(ps)
        cvh = jarvis_march.convex_hull()
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
    
    elif choice == 2:
        pygame.display.set_caption("Line Segment Intersection Demo")
        screen = pygame.display.set_mode((width, height))
        graham_scan = cv.GrahamScan(ps)
        cvh = graham_scan.convex_hull_graham_scan()
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
    
    elif choice == 3:
        pygame.display.set_caption("Line Segment Intersection Demo")
        screen = pygame.display.set_mode((width, height))
        qe = cv.QuickElimination(ps)
        cvh = qe.quick_elimination()
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
    
        
    else:
        print("INVALID")