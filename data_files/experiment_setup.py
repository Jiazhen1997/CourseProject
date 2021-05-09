import sys
from expr.weighted_hs import WeightedLGBPHS

from facerec_py.facerec.distance import *
from facerec_py.facerec.classifier import NearestNeighbor, SVM
from facerec_py.facerec.model import PredictableModel, FeaturesEnsemblePredictableModel
from facerec_py.facerec.validation import KFoldCrossValidation, shuffle
from facerec_py.facerec.visual import subplot
from facerec_py.facerec.util import minmax_normalize
from expr.read_dataset import read_images
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from expr.feature import *
from util.commons_util.logger_utils.logger_factory import LoggerFactory
from scipy.interpolate import spline
import numpy as np

__author__ = 'Danyang'


class Drawer(object):
    def __init__(self, smooth=False):
        plt.figure("R"O"C"")""
"" "" "" "" "" "" "" "" ""p""l""t"".""a""x""i""s""(""[""0"","" ""0"".""5"","" ""0"".""5"","" ""1"".""0""0""1""]"")""
"" "" "" "" "" "" "" "" ""#"" ""a""x"" ""="" ""p""y""p""l""o""t"".""g""c""a""("")""
"" "" "" "" "" "" "" "" ""#"" ""a""x"".""s""e""t""_""a""u""t""o""s""c""a""l""e""_""o""n""(""F""a""l""s""e"")""
"" "" "" "" "" "" "" "" ""p""l""t"".""x""l""a""b""e""l""(""'""F""P""R""'"")""
"" "" "" "" "" "" "" "" ""p""l""t"".""y""l""a""b""e""l""(""'""T""P""R""'"")""
"" "" "" "" "" "" "" "" ""#"" ""c""o""l""o""r""s"":"" ""h""t""t""p"":""/""/""s""t""a""c""k""o""v""e""r""f""l""o""w"".""c""o""m""/""q""u""e""s""t""i""o""n""s""/""2""2""4""0""8""2""3""7""/""n""a""m""e""d""-""c""o""l""o""r""s""-""i""n""-""m""a""t""p""l""o""t""l""i""b""
"" "" "" "" "" "" "" "" ""p""l""t"".""r""c""(""'""a""x""e""s""'"","" ""c""o""l""o""r""_""c""y""c""l""e""=""[""'""r""'"","" ""'""g""'"","" ""'""b""'"","" ""'""c""'"","" ""'""m""'"","" ""'""y""'"","" ""'""k""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""d""a""r""k""g""r""e""e""n""'"","" ""'""c""h""o""c""o""l""a""t""e""'"","" ""'""d""a""r""k""s""a""l""m""o""n""'"","" ""'""d""a""r""k""s""e""a""g""r""e""e""n""'"","" ""'""y""e""l""l""o""w""g""r""e""e""n""'""]"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""i""s""_""s""m""o""o""t""h"" ""="" ""s""m""o""o""t""h""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""r""o""c""s"" ""="" ""[""]""
""
"" "" "" "" ""d""e""f"" ""s""h""o""w""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""p""l""t"".""l""e""g""e""n""d""(""h""a""n""d""l""e""s""=""s""e""l""f"".""_""r""o""c""s"")""
"" "" "" "" "" "" "" "" ""p""l""t"".""s""h""o""w""("")""
""
"" "" "" "" ""d""e""f"" ""p""l""o""t""_""r""o""c""(""s""e""l""f"","" ""c""v"")"":""
"" "" "" "" "" "" "" "" 
        
        FPRs = [r.FPR for r in cv.validation_results]
        TPRs = [r.TPR for r in cv.validation_results]

        
        FPRs.append(0.0)
        TPRs.append(0.0)
        FPRs.append(1.0)
        TPRs.append(1.0)

        if self.is_smooth:
            FPRs, TPRs = self.smooth(FPRs, TPRs)

        
        roc, = plt.plot(FPRs, TPRs, label=cv.model.feature.short_name())
        self._rocs.append(roc)

    def smooth(self, x, y):
        x = np.array(x)
        y = np.array(y)
        x, idx = np.unique(x, return_index=True)  
        y = y[idx]

        x_sm = np.linspace(x.min(), x.max(), 60)  
        y_sm = spline(x, y, x_sm)
        return x_sm, y_sm


class Experiment(object):
    def __init__(self, smooth=False, froze_shuffle=False):
        
        self.logger = LoggerFactory().getConsoleLogger("f"a"c"e"r"e"c"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""d""r""a""w""e""r"" ""="" ""D""r""a""w""e""r""(""s""m""o""o""t""h"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""X"","" ""s""e""l""f"".""y"" ""="" ""s""h""u""f""f""l""e""(""*""s""e""l""f"".""r""e""a""d""("")"")"" "" ""#"" ""s""h""u""f""f""l""e"" ""o""n""c""e""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""f""r""o""z""e""_""s""h""u""f""f""l""e"" ""="" ""f""r""o""z""e""_""s""h""u""f""f""l""e"" "" ""#"" ""w""h""e""t""h""e""r"" ""t""o"" ""f""r""o""z""e"" ""t""h""e"" ""s""u""b""s""e""q""u""e""n""t"" ""s""h""u""f""f""l""i""n""g"" ""i""n"" ""v""a""l""i""d""a""t""i""o""n""
""
"" "" "" "" ""d""e""f"" ""r""e""a""d""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""#"" ""T""h""i""s"" ""i""s"" ""w""h""e""r""e"" ""w""e"" ""w""r""i""t""e"" ""t""h""e"" ""i""m""a""g""e""s"","" ""i""f"" ""a""n"" ""o""u""t""p""u""t""_""d""i""r"" ""i""s"" ""g""i""v""e""n""
"" "" "" "" "" "" "" "" ""#"" ""i""n"" ""c""o""m""m""a""n""d"" ""l""i""n""e"":""
"" "" "" "" "" "" "" "" ""o""u""t""_""d""i""r"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" ""#"" ""Y""o""u""'""l""l"" ""n""e""e""d"" ""a""t"" ""l""e""a""s""t"" ""a"" ""p""a""t""h"" ""t""o"" ""y""o""u""r"" ""i""m""a""g""e"" ""d""a""t""a"","" ""p""l""e""a""s""e"" ""s""e""e""
"" "" "" "" "" "" "" "" ""#"" ""t""h""e"" ""t""u""t""o""r""i""a""l"" ""c""o""m""i""n""g"" ""w""i""t""h"" ""t""h""i""s"" ""s""o""u""r""c""e"" ""c""o""d""e"" ""o""n"" ""h""o""w"" ""t""o"" ""p""r""e""p""a""r""e""
"" "" "" "" "" "" "" "" ""#"" ""y""o""u""r"" ""i""m""a""g""e"" ""d""a""t""a"":""
"" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""s""y""s"".""a""r""g""v"")"" ""<"" ""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t"" 
        draw fisher face components
        color map: http://matplotlib.org/examples/color/colormaps_reference.html
        :param X: images
        :param model: fisher face model
        :param r: number of rows
        :param c: number of cols
        :return:
        
        Define the Fisherfaces as Feature Extraction method

        :param feature: feature extraction
        :param plot: function to plot
        :param dist_metric: distance metric
        :param threshold_up: threshold for ROC
        :param kNN_k: k for kNN classifier
        :param debug: if true, display the images of wrongly classified face
        :return:
        
        Plot the graph at the end
        :return:
        
        Plot a individual result
        :param cv:
        :return:
        
    set threshold_up=1
    :param expr:
    :return:
    