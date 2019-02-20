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
    pass