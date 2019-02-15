import pyoptclass.classes as classes
import numpy as np

def sortByX(element):
    '''
        In situ sort (more or less) by X attr.
        INPUT: list or np.array of Point2D class.
        RETURN: void.
    '''
    if type(element) != list and type(element) != np.array:
        raise ValueError('Must be list or array.')
    return element.sort()

def sortByY(element):
    '''
        In situ sort (more or less) by y element.
        INPUT: list or np.array of Point2D class.
        RETURN: void.
    '''
    if type(element) != list and type(element) != np.array:
        raise ValueError('Must be list or array.')
    return element.sort(key=lambda x: x.Y)