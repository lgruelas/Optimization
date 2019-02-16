import pyoptclass.classes as classes

def test_Point2D():
    point_int = classes.Point2D(3,4)
    point_float = classes.Point2D(3.5, 2.1)
    errors = []
    if not (point_int.X == 3 and point_int.Y == 4):
        errors.append('error')
    if not (point_float.X == 3.5 and point_float.Y == 2.1):
        errors.append('error')
    if not (point_float.__repr__() == '(3.50, 2.10)' and point_int.__repr__() == '(3.00, 4.00)'):
        errors.append('error')
    assert not errors
    