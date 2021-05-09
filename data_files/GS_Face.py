

import numpy as np
from Kernel import Kernel
import numpy.matlib as Nmat
import numpy.linalg as LA


class GsFace(object):
    def __init__(self, X_tar, X_src):
        
        n_src, n_ftr1 = X_src.shape
        n_tar, n_ftr2 = X_tar.shape
        assert n_ftr1 == n_ftr2, 'the dimension of the X_src and the X_tar is not equal'
        n_ftr = n_ftr1
        self.theta = np.zeros([n_ftr + 2, 1])
        self.X_tar = X_tar
        self.X_src = X_src

    def P_prior(self, X, K):
        
        n_data, n_ftr = X.shape
        return 1 / np.sqrt(((2 * np.pi) ** (n_ftr * n_data)) * (LA.det(K) ** n_ftr)) * np.exp(
            -0.5 * (np.trace(K * X * X.T)))

    def KFDA_J(self, K, N_p, N_n, q=0):
        
        if q==0:
            q = N_p + N_n  
        a = Nmat.ones([N_p + N_n, 1])
        a[0:N_p] = 1 / N_p
        a[N_p:] = -1 / N_n
        A = Nmat.matrix([np.diag(1 / np.sqrt(N_p) * (Nmat.identity(N_p) - 1 / N_p * Nmat.ones([N_p, N_p]))), \
                         np.diag(1 / np.sqrt(N_n) * (Nmat.identity(N_n) - 1 / N_n * Nmat.ones([N_n, N_n])))])

        
        
        Q = K
        

        
        tmp = 1e8 * Nmat.identity(N_p + N_n) - 1e8 * A * Q * LA.inv(1e8 * Nmat.identity(q) + Q.T * A * A(Q)) * Q.T * A
        J = 1/1e-8 * (a.T * K * a - a.T * K * A * tmp * A * K * a)
        return J

    def P_latent(self, J, delta):
        
        
        
        
        
        return np.exp(-J / (delta ** 2))

    def P_theta(self):
        p = 1
        for i in range(len(self.theta)):
            p = p * self.theta[i]
        return p

    
    
    

    def P_poster(self, X, K, J, delta):
        n_data, n_ftr = X.shape
        log_prior = n_ftr / 2 * np.log(LA.det(K)) + 0.5 * np.trace(K * X * X.T)

        tmp = 0
        for i in range(len(self.theta)):
            tmp = tmp + np.log(self.theta[i])
        log_theta = tmp

        log_latent = -J / (delta ** 2)
        return log_prior + log_theta + log_latent

    def Gs_model(self, delta, beta, N_ps, N_ns, N_pt, N_nt, q=0):
        

        X_ts = np.append(self.X_tar, self.X_src)

        K_t = Kernel(self.X_tar, self.theta)
        J_t = self.KFDA_J(K_t, N_pt, N_nt, q)
        log_pt = np.log(self.P_poster(self.X_tar, K_t, J_t, delta))
        pt = self.P_poster(self.X_tar, K_t, J_t, N_pt, N_nt, q)  

        K_ts = Kernel(X_ts, self.theta)
        J_ts = self.KFDA_J(K_ts, N_ps + N_pt, N_ns + N_nt, q)
        log_pts = np.log(self.P_poster(X_ts, K_ts, J_ts, delta))
        pts = self.P_poster(X_ts, K_ts, J_ts, N_ps, N_ns, q)  

        K_s = Kernel(self.X_src, self.theta)
        J_s = self.KFDA_J(K_s, N_ps, N_ns, q)
        log_ps = np.log(self.P_poster(self.X_src, K_s, J_s, delta))
        

        Lmodl = -log_pt + beta * pt * log_pt + beta * (pts * log_ps - pts * log_pts)
        return Lmodl