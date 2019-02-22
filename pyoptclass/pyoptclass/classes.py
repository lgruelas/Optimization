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

#Remains the problem of remove one element
class ClusterPdV:
    def __init__(self, centroid=[], pdvs=None):
        self.centroid = centroid
        self._elements = pdvs or []
        self.total_time = 0
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)
        for i in pdvs:
            self.total_time += i.time_store
    def __repr__(self):
        return "["+ ", ".join([str(i) for i in self._elements]) +"]"
    def elements(self):
        for i in self._elements:
            yield i
    def push_back(self, pdv):
        self.total_time += pdv.time_store
        self._elements.append(pdv)
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)
    def convex_hull(self):
        return self._convex_hull
    def area(self):
        return self._area
    def size(self):
        return len(self._elements)


