import math


class Circle:
    def __init__(self, radius):
        self.r = radius

    def diameter(self):
        return 2 * self.r

    def circumference(self):
        return 2 * self.r * math.pi

    def area(self):
        return self.r ** 2 * math.pi


class CircleCoord(Circle):
    def __init__(self, point, r):
        super().__init__(r)
        self.c_x, self.c_y = point

    def contains(self, point):
        x, y = point
        if (self.c_x - x) ** 2 + (self.c_y - y) ** 2 <= self.r ** 2:
            return True
        else:
            return False

    def intersects(self, other):
        if (self.c_x - other.c_x) ** 2 + (self.c_y - other.c_y) ** 2 < (self.r + other.r) ** 2:
            return True
        else:
            return False
