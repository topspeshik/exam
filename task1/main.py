class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class DistanceMeter:
    def __init__(self):
        self.points = []

    def add(self, other: Point):
        self.points.append(other)

    def dist_to(self, point1: Point, point2: Point):
        return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** 0.5

    def measure(self):
        result = 0
        for i in range(len(self.points) - 1):
            result += self.dist_to(self.points[i], self.points[i + 1])
        return result


meter = DistanceMeter()
meter.add(Point(0, 0))
meter.add(Point(2, 0))
meter.add(Point(2, 3))
print(meter.measure())