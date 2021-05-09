import numpy as np
from scipy.stats import logistic
import matplotlib.pyplot as plt

class LogisticRegressioner(object):
    def __init__(self, tol=1e-6):
        self.tol = tol

    def first_derivative(self, X, Y, w):
        
        d, T = X.shape
        sigma = logistic.cdf(np.multiply(-Y, np.dot(w.T, X)))
        ret = np.multiply(sigma, Y)
        ret = np.multiply(np.repeat(ret[np.newaxis, :], d, axis=0), X)
        ret = np.sum(ret, axis=1)
        return ret

    def log_loss(self, X, Y, w):
        L = np.log(logistic.cdf(np.multiply(Y, np.dot(w.T, X))))
        L = np.sum(L)
        L = -L
        return L

    def classifier_w(self, X, Y,eta=0.05):
        
        X = X.T
        d, T = X.shape
        X = np.vstack([np.ones((T, )), X])  
        d += 1
        w = np.zeros(d)
        t = 0
        while True:
            t += 1
            w_ = w + eta*self.first_derivative(X, Y, w)
            L_old, L_new = self.log_loss(X, Y, w_), self.log_loss(X, Y, w)
            if np.abs(L_old - L_new) < self.tol: break
            w = w_
            if t % 300 == 1: yield w  

        yield w

    def test_sample(self):
        X = np.array([
            [2, 1],
            [1, 20],
            [1, 5],
            [4, 1],
            [1, 40],
            [3, 30],
        ])

        Y = np.array([
            -1,
            -1,
            -1,
            1,
            1,
            1,
        ])
        ws = list(self.classifier_w(X, Y))
        print ws[-1]
