from pyoptclass import classes as cl

def test_Point2D():
    point_int = cl.Point2D(3, 4)
    point_float = cl.Point2D(3.5, 2.1)
    errors = []
    if not (point_int.X == 3 and point_int.Y == 4):
        errors.append('error')
    if not (point_float.X == 3.5 and point_float.Y == 2.1):
        errors.append('error')
    if not (point_float.__repr__() == '(3.50, 2.10)' and point_int.__repr__() == '(3.00, 4.00)'):
        errors.append('error')
    assert not errors

def test_PdV():
    point_int = cl.PdV(3, 4, 85.9)
    point_float = cl.PdV(3.5, 2.1, 62.5)
    point_float2 = cl.PdV(3.5, 2.1, 61.5)
    errors = []
    if not (point_int.X == 3 and point_int.Y == 4):
        errors.append('error')
    if not (point_float.X == 3.5 and point_float.Y == 2.1):
        errors.append('error')
    if not (point_float.__repr__() == '[(3.50, 2.10), 62.50]' and point_int.__repr__() == '[(3.00, 4.00), 85.90]'):
        errors.append('error')
    if not (point_float.samePlace(point_float2)):
        errors.append('error')
    if not (point_float.time_store == 62.5 and point_int.time_store == 85.9):
        errors.append('error')
    assert not errors

def test_Cluster():
    items = [(1, 1), (3, 1), (1, 3), (3, 3), (3, 4)]
    cluster = cl.ClusterPdV([cl.PdV(i[0], i[1], i[1]+1) for i in items])
    errors = []
    if not cluster.total_time == sum([i[1]+1 for i in items]):
        errors.append("error")
    for i, j in zip(cluster.elements(), sorted(items)):
        if i.X != j[0] or i.Y != j[1]:
            errors.append("error")
    if not cluster.area() == 5:
        errors.append("error")
    cluster.push_back(cl.PdV(3, 5, 2))
    if not cluster.total_time == sum([i[1]+1 for i in items]) + 2:
        errors.append("error") 
    if not cluster.size() == 6:
        errors.append("error")
    if not cluster.area() == 6:
        errors.append("error")
    assert not errors



'''
class ClusterPdV:
    def __init__(self, pdvs=[]):
        self._elements = pdvs
        self.total_time = 0
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)
        for i in pdvs:
            self.total_time += i.time_store
    def elements(self):
        for i in self._elements:
            yield i
    def push_back(self, pdv):
        self.total_time += pdv.time_store
        self._elements.appned(pdv)
        self._convex_hull = utils.getConvexHull(self._elements)
        self._area = utils.getConvexPolygonArea(self._convex_hull)
    def pop_back(self):
        self.total_time -= self._elements[-1].time_store
        self._convex_hull = utils.getConvexHull(self._elements[:-1])
        self._area = utils.getConvexPolygonArea(self._convex_hull)
        return self._elements.pop()
    def convex_hull(self):
        return self._convex_hull
    def area(self):
        return self._area
    def size(self):
        return len(self._elements)
'''