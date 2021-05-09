


from Join_Ftr import *
from ReadFile import ReadFile
from GS_Face import GsFace



feature_pth = 'E:\\GPforFR\\data\\lfw_feature5'


instruc_pth_t = 'E:\\GPforFR\\data\\lfw_view1\\pairsDevTrain.txt'  
instruc_pth_s = 'E:\\GPforFR\\data\\lfw_view1\\pairsDevTest.txt'  


num = 5


read_file = ReadFile(instruc_pth_t, num)
X1 = read_file.person_pair() + read_file.person_mispair()

read_file = ReadFile(instruc_pth_s, num)
X2 = read_file.person_pair() + read_file.person_mispair()


gs_feature = Join_Ftr()


Xtar, Ytar = gs_feature.Constrct_XY(feature_pth, X1)
Xsrc, Ysrc = gs_feature.Constrct_XY(feature_pth, X2)

Xt_in, Yt_in = gs_feature.XY_in(Xtar, Ytar)
Xs_in, Ys_in = gs_feature.XY_in(Xsrc, Ysrc)


gsface = GsFace(Xt_in, Xs_in)



