class Point2D:
    def __init__(self, x, y):
        self.X = float(x)
        self.Y = float(y)
    def __repr__(self):
        return "(%.2f, %.2f)" % (self.X, self.Y)
    def __eq__(self, point):
        return self.X == point.X and self.Y == point.Y