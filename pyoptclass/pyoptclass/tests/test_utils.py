import pyoptclass.utils as utils
import pyoptclass.classes as classes
import random

def test_sortByX():
    a = [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(3, 3), classes.Point2D(3, 2.5), classes.Point2D(2.5, 3)]
    errors = []
    random.shuffle(a)
    utils.sortByX(a)
    if not a ==  [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(2.5, 3), classes.Point2D(3, 2.5), classes.Point2D(3, 3)]:
        errors.append('error')
    random.shuffle(a)
    utils.sortByX(a, reverse=True)
    if not a == [classes.Point2D(3, 3), classes.Point2D(3, 2.5), classes.Point2D(2.5, 3), classes.Point2D(2, 2), classes.Point2D(1, 1)]:
        errors.append('error')
    assert not errors

def test_sortByY():
    a = [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(3, 3), classes.Point2D(3, 2.5), classes.Point2D(2.5, 3)]
    errors = []
    random.shuffle(a)
    utils.sortByY(a)
    if not a ==  [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(3, 2.5), classes.Point2D(2.5, 3), classes.Point2D(3, 3)]:
        errors.append('error')
    random.shuffle(a)
    utils.sortByY(a, reverse=True)
    if not a == [classes.Point2D(3, 3), classes.Point2D(2.5, 3), classes.Point2D(3, 2.5), classes.Point2D(2, 2), classes.Point2D(1, 1)]:
        errors.append('error')
    assert not errors

def test_sortByX_exception():
    try:
        utils.sortByX("test")
        utils.sortByX((1,2,3))
        utils.sortByX({1,2,3})
        assert False
    except ValueError:
        assert True

def test_sortByY_exception():
    try:
        utils.sortByY("test")
        utils.sortByY((1,2,3))
        utils.sortByY({1,2,3})
        assert False
    except ValueError:
        assert True

def test_getConvexHull():
    points_set = [classes.Point2D(2.5, 0), classes.Point2D(3.5, 0.5), classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(3, 2.5), classes.Point2D(4, 3), classes.Point2D(2.5, 3), classes.Point2D(3, 3)]
    convex_hull = utils.getConvexHull(points_set)
    assert convex_hull == [classes.Point2D(1, 1), classes.Point2D(2.5, 3), classes.Point2D(4, 3), classes.Point2D(3.5, 0.5), classes.Point2D(2.5, 0)]

def test_turnRight():
    points_set = [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(2.5, 3), classes.Point2D(3, 2.5), classes.Point2D(3, 3)]
    errors = []
    if not utils.turnRight(points_set[:2], points_set[3]):
        errors.append("error")
    if utils.turnRight(points_set[:2], points_set[2]):
        errors.append("error")
    if utils.turnRight(points_set[:2], points_set[4]):
        errors.append("error")
    assert not errors

def test_turnLeft():
    points_set = [classes.Point2D(1, 1), classes.Point2D(2, 2), classes.Point2D(2.5, 3), classes.Point2D(3, 2.5), classes.Point2D(3, 3)]
    errors = []
    if not utils.turnLeft(points_set[:2], points_set[2]):
        errors.append("error")
    if utils.turnLeft(points_set[:2], points_set[3]):
        errors.append("error")
    if utils.turnLeft(points_set[:2], points_set[4]):
        errors.append("error")
    assert not errors