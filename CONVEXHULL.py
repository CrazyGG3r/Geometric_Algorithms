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
            return

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
        screen.fill((0, 0, 0))

        for i in range(len(self.hull) - 1):
            self.hull[i].draw_to_point(screen, self.hull[i + 1], color=(0, 255, 0), width=2)
        if len(self.hull) > 1:
            self.hull[-1].draw_to_point(screen, self.hull[0], color=(0, 255, 0), width=2)

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















