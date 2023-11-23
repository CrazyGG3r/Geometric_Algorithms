from functools import cmp_to_key
from itertools import combinations
import CLASSES as c
import math
import pygame 
pygame.init()
class JarvisMarch:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def leftmost_point(self):
        leftmost = 0
        for i in range(1, len(self.points)):
            if self.points[i].x < self.points[leftmost].x:
                leftmost = i
            elif self.points[i].x == self.points[leftmost].x:
                if self.points[i].y > self.points[leftmost].y:
                    leftmost = i
        return leftmost

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0  # Co-linear
        elif val > 0:
            return 1  # Clockwise
        return 2  # Counterclockwise

    def next_hull_point(self, p):
        q = (p + 1) % len(self.points)
        for i in range(len(self.points)):
            if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                q = i
        return q

    def compute_convex_hull(self):
        if len(self.points) < 3:
            return

        leftmost = self.leftmost_point()
        p = leftmost
        while True:
            self.hull.append(p)
            q = self.next_hull_point(p)
            if q == leftmost:
                break
            p = q

def miny(p):
    mini = 0
    min_y_value = p[0][1]  # Assuming the second element of the tuple is the y-coordinate
    for n, a in enumerate(p):
        if a[1] < min_y_value:  # Compare y-coordinates
            mini = n
            min_y_value = a[1]
    return mini

def leftorright(p1, p2, coords):
    # Handle vertical lines
    if p1[0] == p2[0]:
        return coords[0] <= p1[0]
    else:
        m = (p1[1] - p2[1]) / (p1[0] - p2[0])
        x = ((coords[1] - p1[1]) / m) + p1[0]
        return coords[0] <= x
    

    
class bf:
    def __init__(self,p ):
        self.points = p
        #(x,y)
        self.minxindex = miny(self.points)
        self.hull = []
        self.left = []
        self.right = []
    
    def addleft(self):
       
        
        count  = 0 
        p1 =self.points[self.minxindex]
        for n,p2 in  enumerate(self.points):
            if p2 in self.hull:
                continue
            for n,a in enumerate(self.points):
                if a in self.hull:
                    continue
                if leftorright(p1,p2,a):
                    self.left.append(a)
                    count +=1
                else:
                    self.right.append(a)
        
    def addglow(self,screen):
        p = c.point(0,0,(0,255,255),5)
        once = 0
        for a in self.left:
            if once == 1:
                break
            #p.draw(screen)
            #p.update_coords(a[1])
            print(a)
        once = 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                  return
        
        
                    
                    





class QuickElimination:
    def __init__(self, points):
        self.points = points

    def sort_points(self):
        self.points.sort(key=lambda p: p.x)

    def is_right(self, p1, p2, p3):
        det = (p3.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p3.x - p1.x)
        return det < 0

    def quick_elimination(self):
        hull = []
        self.sort_points()

        # Add the first two points to the hull
        hull.append(self.points[0])
        hull.append(self.points[1])

        for i in range(2, len(self.points)):
            while len(hull) >= 2 and not self.is_right(hull[-2], hull[-1], self.points[i]):
                hull.pop()

            hull.append(self.points[i])

        return hull















