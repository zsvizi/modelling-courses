import math


class Circle:
    def __init__(self, radius):
        self.r = radius

    def diameter(self):
        return 2*self.r

    def circumference(self):
        return 2 * self.r * math.pi

    def area(self):
        return (self.r ** 2) * math.pi


class CircleCoord(Circle):
    def __init__(self, radius, center_x, center_y):
        super().__init__(radius=radius)
        self.c_x = center_x
        self.c_y = center_y

    def contains(self, point):
        p_x, p_y = point
        if (p_x - self.c_x) ** 2 + (p_y - self.c_y) ** 2 <= self.r ** 2:
            return True
        else:
            return False

    def overlaps(self, other_circle):
        if (other_circle.c_x - self.c_x) ** 2 + (other_circle.c_y - self.c_y) ** 2 <= (self.r + other_circle.r) ** 2:
            return True
        else:
            return False
