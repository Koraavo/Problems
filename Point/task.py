class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return (((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)) ** 0.5


# p1 = Point(1.5, 1)
# p2 = Point(1.5, 2)
#
# print(p1.dist(p2))
