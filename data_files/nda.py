import numpy as np
import math
from sklearn.neighbors import NearestNeighbors as nn
from facerec_py.facerec.feature import *
from facerec_py.facerec.util import *

__author__ = "X"i"n"g"J"i"a""
""
""c""l""a""s""s"" ""t""r""a""i""n""("")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""a""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""l""a""b""e""l""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""i""m"" ""="" ""0""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""N"" ""="" ""0""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""t""o""t""a""l""C""l""a""s""s"" ""="" ""0""
""
""c""l""a""s""s"" ""N""D""A""F""i""s""h""e""r""(""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""n""u""m""_""c""o""m""p""o""n""e""n""t""s""=""1""0""0"")"":""
"" "" "" "" "" "" "" "" ""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"".""_""_""i""n""i""t""_""_""(""s""e""l""f"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""n""u""m""_""c""o""m""p""o""n""e""n""t""s"" ""="" ""n""u""m""_""c""o""m""p""o""n""e""n""t""s""
""
"" "" "" "" ""d""e""f"" ""c""o""m""p""u""t""e""(""s""e""l""f"","" ""X"","" ""y"")"":""
"" "" "" "" "" "" "" "" ""n""d""a"" ""="" ""N""D""A""("")""
"" "" "" "" "" "" "" "" ""p""c""a"" ""="" ""P""C""A""(""s""e""l""f"".""_""n""u""m""_""c""o""m""p""o""n""e""n""t""s"")""
"" "" "" "" "" "" "" "" ""m""o""d""e""l"" ""="" ""C""h""a""i""n""O""p""e""r""a""t""o""r""(""p""c""a"","" ""n""d""a"")""
"" "" "" "" "" "" "" "" ""m""o""d""e""l"".""c""o""m""p""u""t""e""(""X"","" ""y"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""e""i""g""e""n""v""e""c""t""o""r""s"" ""="" ""n""p"".""d""o""t""(""p""c""a"".""e""i""g""e""n""v""e""c""t""o""r""s"","" ""n""d""a"".""W"".""T"")""
"" "" "" "" "" "" "" "" ""f""e""a""t""u""r""e""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""x"" ""i""n"" ""X"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""x""p"" ""="" ""s""e""l""f"".""p""r""o""j""e""c""t""(""x"".""r""e""s""h""a""p""e""(""-""1"","" ""1"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""e""a""t""u""r""e""s"".""a""p""p""e""n""d""(""x""p"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""f""e""a""t""u""r""e""s""
""
"" "" "" "" ""d""e""f"" ""e""x""t""r""a""c""t""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""X"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""X"")"".""r""e""s""h""a""p""e""(""-""1"","" ""1"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""p""r""o""j""e""c""t""(""X"")""
""
"" "" "" "" ""d""e""f"" ""p""r""o""j""e""c""t""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""p"".""d""o""t""(""s""e""l""f"".""_""e""i""g""e""n""v""e""c""t""o""r""s"".""T"","" ""X"")""
""
""
""
""c""l""a""s""s"" ""N""D""A""(""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"".""_""_""i""n""i""t""_""_""(""s""e""l""f"")""
""
"" "" "" "" ""d""e""f"" ""c""o""m""p""u""t""e""(""s""e""l""f"","" ""X"","" ""y"","" ""K""=""1"","" ""u""s""e""w""e""i""g""h""t""s""=""0"")"":""
"" "" "" "" "" "" "" "" 
        self.train = train()
        self.train.mat = np.array(X)
        self.train.mat = asColumnMatrix(X) 
        self.train.labels = y   
        self.train.N = np.size(X, 0)  
        self.train.dim = np.size(X, 1) 
        self.train.totalClass = len(np.unique(y)) 
        self.K = K

        self.dim = np.size(X, 1)
        self.origdim = self.train.dim
        self.N = np.size(X, 0)
        self.totalClass = self.train.totalClass
        self.meandata = np.mean(self.train.mat, 1, dtype='float64')
        self.train.mat = self.train.mat - np.dot(self.meandata, np.ones((1, self.train.N)))

        self.indIn = np.zeros((K, self.N))
        self.indEx = np.zeros((K, self.N))
        self.valIn = np.zeros((K, self.N))
        self.valEx = np.zeros((K, self.N))

        self.compute_within_class_matrix_whitening()
        self.mnnInn = self.compute_within_class_scatter_matrix()
        self.diffIntra = self.train.mat - self.mnnInn
        self.Wscat = np.dot(self.diffIntra, self.diffIntra.transpose())/self.diffIntra.shape[1]
        self.eval, self.evec = np.linalg.eig(self.Wscat)
        self.ind = np.argsort(self.eval, 0)
        self.eval = self.eval[self.ind]
        self.eval = np.flipud(self.eval)
        self.ind = np.flipud(self.ind)
        self.evec = self.evec[:, self.ind]
        self.wdim = np.max(np.nonzero(self.eval > math.pow(10, -8))).real
        self.evec = self.evec[:, 0:self.wdim]
        self.whiteMat = np.dot(np.diag(1/np.sqrt(self.eval[0:self.wdim])), self.evec.transpose())
        self.Wtr = np.dot(self.whiteMat, self.train.mat)

        self.compute_bet_class_cluster_dist()
        self.mnnEx = self.compute_bet_class_cluster_matrix()
        self.diffExtra = self.Wtr - self.mnnEx
        if useweights:
            self.weights = np.minimum(self.valIn[self.K-1, :], self.valEx[self.K-1, :])
            temp = np.ones((self.Wtr.shape[1],))
            temp = np.dot(temp, self.weights)
            temp = temp * self.diffExtra
            self.bscat = np.dot(temp, np.transpose(self.diffExtra)) / self.N
        else:
            self.bscat = np.dot(self.diffExtra, self.diffExtra.conj().transpose())/self.N
        self.eigval, self.evec = np.linalg.eig(self.bscat)

        self.ind = np.argsort(self.eigval)
        self.val = self.eigval[self.ind]
        self.ind = np.flipud(self.ind)
        self.eigval = self.eigval[self.ind]
        self.eigvec = self.evec[:, self.ind[0:min(self.dim, self.wdim)]]
        self.mat = np.dot(self.eigvec.conj().transpose(), self.Wtr)
        self.W = np.dot(self.eigvec.conj().transpose(), self.whiteMat)
        self.proymat = self.W

        features = []
        for x in X:
            
            xp = self.project(x.reshape(-1, 1))
            features.append(xp)
        return features


    def compute_bet_class_cluster_dist(self):
        
        for x in np.unique(self.train.labels):
            
            who_cl = np.where(self.train.labels == x)[0]
            who_notcl = np.where((self.train.labels != x))[0]
            self.data_intra = self.Wtr[:, who_cl]
            self.data_extra = self.Wtr[:, who_notcl]

            knn = nn().fit(self.data_extra.transpose())
            self.dextra, self.indextra = knn.kneighbors(self.data_intra.transpose())
            self.dextra = self.dextra.transpose()
            self.indextra = self.indextra.transpose()
            self.indEx[:, who_cl] = who_notcl[self.indextra[1, :]]
            self.valEx[:, who_cl] = self.dextra[1, :]

    def compute_bet_class_cluster_matrix(self):
        if self.K == 1:
            mnnEx = self.Wtr[:, map(lambda x: int(x), self.indEx[0, :])]
        else:
            mnnEx = np.zeros((np.size(self.Wtr, 0), self.train.N))
            for n in range(0, self.train.N):
                mnnEx[:, n] == np.mean(self.Wtr[:, map(lambda x: int(x), self.indEx[:, n])], 1)
        return mnnEx

    def compute_within_class_matrix_whitening(self):
        
        for x in np.unique(self.train.labels):
            who_cl = np.where(self.train.labels == x)[0]
            self.data_intra = self.train.mat[:, who_cl]
            knn = nn().fit(self.data_intra.transpose())
            self.dintra, self.indintra = knn.kneighbors(self.data_intra.transpose())
            self.dintra = self.dintra.transpose()
            self.indintra = self.indintra.transpose()
            self.dintra[self.K, :] = []
            self.indintra[self.K, :] = []
            self.valIn[:, who_cl] = self.dintra[1, :]
            self.indIn[:, who_cl] = who_cl[self.indintra[1, :]]

    def compute_within_class_scatter_matrix(self):
        if self.K == 1:
            mnnInn = self.train.mat[:, map(lambda x: int(x), self.indIn[0])]
        else:
            mnnInn = np.zeros((self.train.dim, self.train.N))
            for n in range(0, self.train.N):
                mean = np.mean(self.train.mat[:, map(lambda x: int(x), self.indIn[:, n])], 1)
                for x in range(0, self.train.dim):
                    mnnInn[x, n] = mean[x]
        return mnnInn

    def extract(self, X):
        X = np.asarray(X).reshape(-1, 1)
        return self.project(X)

    def project(self, X):
        return np.dot(self.W, X)

    def __repr__(self):
        return "N"D"A""
""
""
""
""
""
""
""
""
""
""
""
