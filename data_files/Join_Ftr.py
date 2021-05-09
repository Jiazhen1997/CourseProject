

import pickle
import numpy as np
import os.path
import numpy.matlib as mat


class Join_Ftr(object):
    def Join_feature(self, fl1, fl2):
        
        

        
        ftr1 = pickle.load(fl1)
        ftr2 = pickle.load(fl2)

        
        
        
        
        
        
        
        row, col = ftr1.shape
        jnt_ftr = np.empty([5, col * 2])
        for i in range(5):
            jnt_ftr[i] = np.append(ftr1[i], ftr2[i])
        
        
        
        return jnt_ftr

    def Constrct_XY(self, feature_pth, X_info):
        


        X = []
        Y = []

        for i in range(len(X_info)):
            pth1 = os.path.join(feature_pth, X_info[i][0])
            pth2 = os.path.join(feature_pth, X_info[i][1])
            if os.path.exists(pth1) and os.path.exists(pth2):
                fl1 = open(pth1, 'r')
                fl2 = open(pth2, 'r')

                X.append(self.Join_feature(fl1, fl2))
                Y.append(X_info[i][2])
                fl1.close()
                fl2.close()

        return X, Y

    def XY_in(self, X, Y):
        
        assert len(X) == len(Y), "t"h"e" "n"u"m"b"e"r" "o"f" "t"h"e" "i"m"a"g"e" "p"a"i"r" "a"n"d" "t"h"e"i"r" "c"o"r"r"e"s"p"o"n"d"i"n"g" "y" "i"s" "n"o"t" "e"q"u"a"l""
"" "" "" "" "" "" "" "" ""n""u""m""_""o""f""_""p""a""i""r"" ""="" ""l""e""n""(""X"")""
"" "" "" "" "" "" "" "" ""n""u""m""_""o""f""_""p""a""t""c""h"" ""="" ""X""[""0""]"".""s""h""a""p""e""[""0""]""
"" "" "" "" "" "" "" "" ""n""_""f""t""r"" ""="" ""X""[""0""]"".""s""h""a""p""e""[""1""]""
"" "" "" "" "" "" "" "" ""X""_""i""n"" ""="" ""m""a""t"".""z""e""r""o""s""(""[""n""u""m""_""o""f""_""p""a""i""r"" ""*"" ""n""u""m""_""o""f""_""p""a""t""c""h"" ""*"" ""2"","" ""n""_""f""t""r""]"")""
"" "" "" "" "" "" "" "" ""Y""_""i""n"" ""="" ""m""a""t"".""z""e""r""o""s""(""[""n""u""m""_""o""f""_""p""a""i""r"" ""*"" ""n""u""m""_""o""f""_""p""a""t""c""h"" ""*"" ""2"","" ""1""]"")""
"" "" "" "" "" "" "" "" ""n""u""m"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""n""u""m""_""o""f""_""p""a""i""r"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""m""g""_""p""a""i""r"" ""="" ""X""[""i""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""n""u""m""_""o""f""_""p""a""t""c""h"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""X""_""i""n""[""n""u""m""]"" ""="" ""i""m""g""_""p""a""i""r""[""j""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""Y""_""i""n""[""n""u""m""]"" ""="" ""Y""[""i""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""n""u""m"" ""="" ""n""u""m"" ""+"" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""X""_""i""n""[""n""u""m"","" ""0"":""n""_""f""t""r"" ""/"" ""2""]"" ""="" ""i""m""g""_""p""a""i""r""[""j""]""[""n""_""f""t""r"" ""/"" ""2"":""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""X""_""i""n""[""n""u""m"","" ""n""_""f""t""r"" ""/"" ""2"":""]"" ""="" ""i""m""g""_""p""a""i""r""[""j""]""[""0"":""n""_""f""t""r"" ""/"" ""2""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""Y""_""i""n""[""n""u""m""]"" ""="" ""Y""[""i""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""n""u""m"" ""="" ""n""u""m"" ""+"" ""1""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""X""_""i""n"","" ""Y""_""i""n""
"" "" "" "" ""
