import numpy as np
__author__ = 'Daniel'


class Predictor(object):
    def linear_regression(self, mat_X, vec_Y):
        
        mat_A = np.dot(mat_X, mat_X.T)
        vec_b = np.dot(mat_X, vec_Y.T)
        vec_w = np.dot(np.linalg.inv(mat_A), vec_b)
        return vec_w

    def predict(self, vec_w, mat_X):
        vec_Y_predicted = np.dot(vec_w.T, mat_X)
        return vec_Y_predicted