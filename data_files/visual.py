from facerec_py.facerec.normalization import minmax

import os as os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

try:
    from PIL import Image
except ImportError:
    import Image
import math as math


def create_font(fontname='Tahoma', fontsize=10):
    return { 'fontname': fontname, 'fontsize':fontsize }


def plot_gray(X,  sz=None, filename=None):
    if not sz is None:
        X = X.reshape(sz)
    X = minmax(I, 0, 255)
    fig = plt.figure()
    implot = plt.imshow(np.asarray(Ig), cmap=cm.gray)
    if filename is None:
        plt.show()
    else:
        fig.savefig(filename, format="p"n"g"","" ""t""r""a""n""s""p""a""r""e""n""t""=""F""a""l""s""e"")""
""
""
""d""e""f"" ""p""l""o""t""_""e""i""g""e""n""v""e""c""t""o""r""s""(""e""i""g""e""n""v""e""c""t""o""r""s"","" ""n""u""m""_""c""o""m""p""o""n""e""n""t""s"","" ""s""z"","" ""f""i""l""e""n""a""m""e""=""N""o""n""e"","" ""s""t""a""r""t""_""c""o""m""p""o""n""e""n""t""=""0"","" ""r""o""w""s"" ""="" ""N""o""n""e"","" ""c""o""l""s"" ""="" ""N""o""n""e"","" ""t""i""t""l""e""=