


import numpy as np


class Kernel:
    def __init__(self, alpha, gammas):
        self.alpha = np.exp(alpha)
        self.gammas = np.exp(gammas)
        self.dim = gammas.size
        self.nparams = self.dim + 1

    def set_params(self, params):
        assert params.size == self.nparams
        self.alpha = np.exp(params).copy().flatten()[0]
        self.gammas = np.exp(params).copy().flatten()[1:]

    def get_params(self):
        
        return np.log(np.hstack((self.alpha, self.gammas)))

    def __call__(self, x1, x2):
        
        if x1.size / len(x1) == 1:
            N1 = 1
            D1 = x1.size
        else:
            N1, D1 = x1.shape
        if x2.size / len(x2) == 1:
            N2 = 1
            D2 = x2.size
        else:
            N2, D2 = x2.shape
        assert D1 == D2, "x"1" "d"i"m"e"n"s"i"o"n" "n"o"t" "e"q"u"a"l" "t"o" "x"2""
"" "" "" "" "" "" "" "" ""a""s""s""e""r""t"" ""D""1"" ""=""="" ""s""e""l""f"".""d""i""m"","" 
        the gradients wrt params
        
        the derivative matrix with regart to the data
        return a list of D matrix(N*N)
        