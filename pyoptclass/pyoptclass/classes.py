from pyoptclass import utils

class Point2D:
    def __init__(self, x, y):
        self.X = float(x)
        self.Y = float(y)
    def __repr__(self):
        return "(%.2f, %.2f)" % (self.X, self.Y)
    def __eq__(self, point):
        return self.X == point.X and self.Y == point.Y

class PdV(Point2D):
    def __init__(self, x, y, time_store):
        Point2D.__init__(self, x, y)
        self.time_store = time_store
    def __repr__(self):
        return "[%s, %.2f]" % (Point2D.__repr__(self), self.time_store)
    def samePlace(self, pdv):
        return self == pdv

class ClusterPdV:
    def __init__(self, pdvs=[]):
        self._elements = pdvs
        self.total_time = 0
        for i in pdvs:
            self.total_time += i.time_store
    def elements(self):
        for i in self._elements:
            yield i
    def push_back(self, pdv):
        self.total_time += pdv.time_store
        self._elements.appned(pdv)
    def pop_back(self):
        self.total_time -= self._elements[-1].time_store
        return self._elements.pop()
    def convex_hull(self):
        return utils.getConvexHull(self._elements)
    def size(self):
        return len(self._elements)
    def area(self):
        pass