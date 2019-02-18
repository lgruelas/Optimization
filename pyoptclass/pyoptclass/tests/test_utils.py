import pyoptclass.utils as utils
import pyoptclass.classes as classes
import random

def test_sortByX():
    a = [classes.Point2D(i, 1-i) for i in xrange(10)]
    random.shuffle(a)
    utils.sortByX(a)
    assert a == [classes.Point2D(i, 1-i) for i in xrange(10)]

def test_sortByY():
    a = [classes.Point2D(i, 1-i) for i in xrange(10)]
    random.shuffle(a)
    utils.sortByY(a)
    assert a == [classes.Point2D(i, 1-i) for i in xrange(9, -1, -1)]

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