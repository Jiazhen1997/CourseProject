from experiment_setup import *
import numpy as np
from expr.kernelpca_ski import KPCA
from util.commons_util.decorators.general import print_func_name

__author__ = 'Danyang'


class Plotter(object):
    def __init__(self):
        pass

    def _plot(self, models, dist_metric=EuclideanDistance()):
        expr = Experiment(froze_shuffle=True)
        for model in models:
            cv = expr.experiment(model, threshold_up=1, debug=False, dist_metric=dist_metric)
            expr.plot_roc(cv)
        expr.show_plot()

    def _simple_run(self, models, dist_metric=EuclideanDistance()):
        expr = Experiment(froze_shuffle=True)
        for model in models:
            expr.experiment(model, threshold_up=0, debug=False, dist_metric=dist_metric)


class PlotterPCA(Plotter):
    def plot_components(self):
        models = []
        for num_component in xrange(10, 150, 30):
            models.append(PCA(num_component))

        self._plot(models)

    def plot_energy(self):
        models = []

        class PCA_energy(PCA):
            def short_name(self):
                return "P"C"A":" "%"."2"f"%"%"" ""%"" ""(""s""e""l""f"".""e""n""e""r""g""y""_""p""e""r""c""e""n""t""a""g""e"" ""*"" ""1""0""0"")""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""n""u""m""_""c""o""m""p""o""n""e""n""t"" ""i""n"" ""x""r""a""n""g""e""(""2""0"","" ""1""1""0"","" ""4""0"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""o""d""e""l""s"".""a""p""p""e""n""d""(""P""C""A""_""e""n""e""r""g""y""(""n""u""m""_""c""o""m""p""o""n""e""n""t"")"")""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""p""l""o""t""(""m""o""d""e""l""s"")""
""
""
""c""l""a""s""s"" ""P""l""o""t""t""e""r""F""i""s""h""e""r""(""P""l""o""t""t""e""r"")"":""
"" "" "" "" ""d""e""f"" ""p""l""o""t""_""c""o""m""p""o""n""e""n""t""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""m""o""d""e""l""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""n""u""m""_""c""o""m""p""o""n""e""n""t""s"" ""i""n"" ""x""r""a""n""g""e""(""1"","" ""1""6"","" ""3"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""o""d""e""l""s"".""a""p""p""e""n""d""(""F""i""s""h""e""r""f""a""c""e""s""(""n""u""m""_""c""o""m""p""o""n""e""n""t""s"")"")""
""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""p""l""o""t""(""m""o""d""e""l""s"")""
""
""
""c""l""a""s""s"" ""P""l""o""t""t""e""r""K""n""n""(""o""b""j""e""c""t"")"":""
"" "" "" "" ""d""e""f"" ""p""l""o""t""_""k""N""N""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" 
        pca = PCA(40)
        expr = Experiment()

        plt.figure("P"C"A" "p"r"e"c"i"s"i"o"n" "f"o"r" "d"i"f"f"e"r"e"n"t" "k" "i"n" "k"N"N"")""
"" "" "" "" "" "" "" "" ""p""l""t"".""x""l""a""b""e""l""(
        varying degrees for poly
        

        :return:
        
        varying kernels
        :return:
        
        varying coef0 values for poly
        
        varying gamma values for poly
        
        varying gamma values for sigmoid
        
        _plot the graph of varying k of kNN
        :return:
        
        _plot the graph of varying k of kNN
        :return:
        
        _plot the graph of varying k of kNN
        :return:
        