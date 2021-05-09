import numpy as np
import numpy.linalg as la


__author__ = 'Danyang'


def transpose(A):
    
    A.transpose()
    return A.T


def inverse(A):
    return la.inv(A)


def to2D(A):
    
    return A[np.newaxis]


def to1D(A):
    
    return A.ravel()


def unroll(A):
    
    return A.reshape(1, -1)

