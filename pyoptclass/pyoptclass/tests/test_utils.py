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
