from pyoptclass import utils
import copy

class Point2D:
    def __init__(self, x, y):
        self.X = float(x)
        self.Y = float(y)

    def __repr__(self):
        return "(%.2f, %.2f)" % (self.X, self.Y)

    def __eq__(self, point):
        return self.X == point.X and self.Y == point.Y

    def __add__(self, y):
        return Point2D(self.X + y.X, self.Y + y.Y)

    def __iadd__(self, y):
        self.X += y.X
        self.Y += y.Y
        return self

    def __sub__(self, y):
        return Point2D(self.X - y.X, self.Y - y.Y)

    def __isub__(self, y):
        self.X -= y.X
        self.Y -= y.Y
        return self

    def __mul__(self, y):
        return Point2D(self.X * y.X, self.Y * y.Y)

    def __imul__(self, y):
        self.X *= y.X
        self.Y *= y.Y
        return self


class PdV(Point2D):
    def __init__(self, x, y, time_store):
        Point2D.__init__(self, x, y)
        self.time_store = time_store

    def __repr__(self):
        return "[%s, %.2f]" % (Point2D.__repr__(self), self.time_store)

    def samePlace(self, pdv):
        return self == pdv


class ClusterPdV:
    def __init__(self, pdvs, centroid=None):
        self.centroid = copy.deepcopy(centroid) or [None, None]
        self._elements = copy.deepcopy(pdvs)
        self.total_time = 0
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)
        for i in pdvs:
            self.total_time += i.time_store

    def __repr__(self):
        return "[" + ", ".join([str(i) for i in self._elements]) + "]"

    def elements(self):
        for i in self._elements:
            yield i

    def push_back(self, pdv):
        self.total_time += pdv.time_store
        self._elements.append(pdv)
        #self._convex_hull = utils.getConvexHull(self._elements)
        #self._area = utils.getConvexPolygonArea(self._convex_hull)

    def remove(self, pdv):
        self.total_time -= pdv.time_store
        self._elements.remove(pdv)
        #if pdv in self._convex_hull:
        #    self._convex_hull = utils.getConvexHull(self._elements)
        #   self._area = utils.getConvexPolygonArea(self._convex_hull)

    def convex_hull(self):
        return self._convex_hull

    def area(self):
        return self._area

    def size(self):
        return len(self._elements)

    def setCenter(self, new):
        if isinstance(new, list) and len(new) == 2:
            self.centroid = new
        else:
            raise ValueError("New center must be a list of length 2.")

    def update(self):
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)


