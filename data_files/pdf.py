import numpy as np

__author__ = 'Danyang'


def parzen_estimation(x_samples, point_x, h):
    
    k_n = 0
    for row in x_samples:
        x_i = (point_x - row[:, np.newaxis]) / h
        for row in x_i:
            if np.abs(row) > 1/2:
                break
        else:  
            k_n += 1

    return (k_n / len(x_samples)) / (h**point_x.shape[1])