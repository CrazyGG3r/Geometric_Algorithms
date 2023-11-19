from functools import cmp_to_key
from itertools import combinations
import CLASSES as c


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









class GrahamScan:
    def __init__(self, points):
        self.points = points
        self.convex_hull = []

    def orientation(self, p, q, r):
        val = ((q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y))
        if val == 0:
            return 0  # collinear
        elif val > 0:
            return 1  # clockwise
        else:
            return 2  # counterclockwise

    def compare(self, p1, p2):
        o = self.orientation(self.p0, p1, p2)
        if o == 0:
            if self.distSq(self.p0, p2) >= self.distSq(self.p0, p1):
                return -1
            else:
                return 1
        else:
            if o == 2:
                return -1
            else:
                return 1

    def distSq(self, p1, p2):
        return ((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))

    def next_to_top(self, S):
        return S[-2]

    def convex_hull_graham_scan(self):
        n = len(self.points)

        if n < 3:
            return

        ymin = self.points[0].y
        min_index = 0

        for i in range(1, n):
            y = self.points[i].y

            if y < ymin or (ymin == y and self.points[i].x < self.points[min_index].x):
                ymin = self.points[i].y
                min_index = i

        self.points[0], self.points[min_index] = self.points[min_index], self.points[0]
        self.p0 = self.points[0]

        self.points = sorted(self.points, key=cmp_to_key(self.compare))

        m = 1
        for i in range(1, n):
            while i < n - 1 and self.orientation(self.p0, self.points[i], self.points[i + 1]) == 0:
                i += 1

            self.points[m] = self.points[i]
            m += 1

        if m < 3:
            return

        S = []
        S.append(self.points[0])
        S.append(self.points[1])
        S.append(self.points[2])

        for i in range(3, m):
            while len(S) > 1 and self.orientation(self.next_to_top(S), S[-1], self.points[i]) != 2:
                S.pop()
            S.append(self.points[i])

        return S

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















