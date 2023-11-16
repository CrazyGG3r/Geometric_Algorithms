from functools import cmp_to_key
from itertools import combinations
import CLASSES as c
import math
class JarvisMarch:
    def __init__(self, points):
        self.points = points

    def left_index(self):
        min_idx = 0
        for i in range(1, len(self.points)):
            if self.points[i].x < self.points[min_idx].x:
                min_idx = i
            elif self.points[i].x == self.points[min_idx].x:
                if self.points[i].y > self.points[min_idx].y:
                    min_idx = i
        return min_idx

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def convex_hull(self):
        n = len(self.points)
        if n < 3:
            return []

        l = self.left_index()
        hull = []
        p = l
        q = 0
        while True:
            hull.append(p)
            q = (p + 1) % n

            for i in range(n):
                if self.orientation(self.points[p], self.points[i], self.points[q]) == 2:
                    q = i

            p = q
            if p == l:
                break

        result = [(self.points[i]) for i in hull]
        return result








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

class QuickHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def find_hull(self):
        if len(self.points) < 3:
            print("Convex hull is not possible with less than 3 points.")
            return

        # Find the leftmost and rightmost points
        min_x, max_x = float('inf'), float('-inf')
        leftmost, rightmost = None, None
        for point in self.points:
            if point.x < min_x:
                min_x = point.x
                leftmost = point
            if point.x > max_x:
                max_x = point.x
                rightmost = point

        self.hull.append(leftmost)
        self.hull.append(rightmost)

        # Split the points into two sets based on which side of the line they lie
        points_left = [point for point in self.points if self.orientation(leftmost, rightmost, point) == 1]
        points_right = [point for point in self.points if self.orientation(leftmost, rightmost, point) == -1]

        # Recursively find the convex hull on each side of the line
        self.find_hull_recursive(leftmost, rightmost, points_left)
        self.find_hull_recursive(rightmost, leftmost, points_right)

        return self.hull
    def find_hull_recursive(self, p1, p2, points):
        if not points:
            return

        # Find the point with maximum distance from the line formed by p1 and p2
        max_distance = 0
        farthest_point = None
        for point in points:
            current_distance = self.distance(p1, p2, point)
            if current_distance > max_distance:
                max_distance = current_distance
                farthest_point = point

        # Add the farthest point to the convex hull
        self.hull.insert(self.hull.index(p2), farthest_point)

        # Split the points into two sets based on which side of the line they lie
        points_left = [point for point in points if self.orientation(p1, farthest_point, point) == 1]
        points_right = [point for point in points if self.orientation(farthest_point, p2, point) == 1]

        # Recursively find the convex hull on each side of the line
        self.find_hull_recursive(p1, farthest_point, points_left)
        self.find_hull_recursive(farthest_point, p2, points_right)

    @staticmethod
    def orientation(p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
        if val == 0:
            return 0
        return 1 if val > 0 else -1

    @staticmethod
    def distance(p1, p2, p):
        return abs((p.y - p1.y) * (p2.x - p1.x) - (p2.y - p1.y) * (p.x - p1.x)) / ((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2) ** 0.5

    















