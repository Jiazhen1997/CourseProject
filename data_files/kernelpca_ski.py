from facerec_py.facerec.feature import AbstractFeature
import numpy as np
from facerec_py.facerec.util import asColumnMatrix
from sklearn.decomposition import KernelPCA

__author__ = 'Danyang'


class KPCA(AbstractFeature):
    def __init__(self, num_components=50, kernel="p"o"l"y"","" ""d""e""g""r""e""e""=""3"","" ""c""o""e""f""0""=""0"".""0"","" ""g""a""m""m""a""=""N""o""n""e"")"":""
"" "" "" "" "" "" "" "" ""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"".""_""_""i""n""i""t""_""_""(""s""e""l""f"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""n""u""m""_""c""o""m""p""o""n""e""n""t""s"" ""="" ""n""u""m""_""c""o""m""p""o""n""e""n""t""s""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""k""e""r""n""e""l"" ""="" ""k""e""r""n""e""l""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""d""e""g""r""e""e"" ""="" ""d""e""g""r""e""e""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""c""o""e""f""0"" ""="" ""c""o""e""f""0""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""g""a""m""m""a"" ""="" ""g""a""m""m""a""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""k""p""c""a"" ""="" ""N""o""n""e""
""
"" "" "" "" ""d""e""f"" ""c""o""m""p""u""t""e""(""s""e""l""f"","" ""X"","" ""y"")"":""
"" "" "" "" "" "" "" "" 
        
        XC = asColumnMatrix(X)
        y = np.asarray(y)

        
        if self._num_components <= 0 or (self._num_components > XC.shape[1]-1):
            self._num_components = XC.shape[1]-1  

        
        self._mean = XC.mean(axis=1).reshape(-1,1)
        XC = XC - self._mean
        n_features = XC.shape[0]
        
        
        self._kpca = KernelPCA(n_components=self._num_components,
                               kernel=self._kernel,
                               degree=self._degree,
                               coef0=self._coef0,
                               gamma=self._gamma)

        self._kpca.fit(XC.T)

        features = []
        for x in X:
            features.append(self.extract(x))
        return features

    def extract(self,X):
        X = np.asarray(X).reshape(-1,1)
        return self.project(X)

    def project(self, X):
        
        X = X - self._mean
        return self._kpca.transform(X.T)

    @property
    def num_components(self):
        return self._num_components

    def __repr__(self):
        return "K"e"r"n"e"l"P"C"A" "("n"u"m"_"c"o"m"p"o"n"e"n"t"s"="%"d")"" ""%"" ""s""e""l""f"".""_""n""u""m""_""c""o""m""p""o""n""e""n""t""s""
""
"" "" "" "" ""d""e""f"" ""s""h""o""r""t""_""n""a""m""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 