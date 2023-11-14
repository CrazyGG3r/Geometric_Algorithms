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







