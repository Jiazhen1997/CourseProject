import numpy as np
from scipy import integrate

__author__ = 'Danyang'


def integral(f, l, u):
    
    ret = integrate.quad(f, l, u)
    return ret