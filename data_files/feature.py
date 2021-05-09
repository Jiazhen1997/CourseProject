import numpy as np


class AbstractFeature(object):
    def compute(self, X, y):
        raise NotImplementedError("E"v"e"r"y" "A"b"s"t"r"a"c"t"F"e"a"t"u"r"e" "m"u"s"t" "i"m"p"l"e"m"e"n"t" "t"h"e" "c"o"m"p"u"t"e" "m"e"t"h"o"d"."")""
""
"" "" "" "" ""d""e""f"" ""e""x""t""r""a""c""t""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""N""o""t""I""m""p""l""e""m""e""n""t""e""d""E""r""r""o""r""(
    Simplest AbstractFeature you could imagine. It only forwards the data and does not operate on it, 
    probably useful for learning a Support Vector Machine on raw data for example!
    
        PCA over the entire images set
        dimension reduction for entire images set


        * Prepare the data with each column representing an image.
        * Subtract the mean image from the data.
        * Calculate the eigenvectors and eigenvalues of the covariance matrix.
        * Find the optimal transformation matrix by selecting the principal components (eigenvectors with largest eigenvalues).
        * Project the centered data into the subspace.
        Reference: http://en.wikipedia.org/wiki/Eigenface

        :param X: The images, which is a Python list of numpy arrays.
        :param y: The corresponding labels (the unique number of the subject, person) in a Python list.
        :return:
        
        Instead of doing one histogram for the whole picture, slice the image into mxn (sz) smaller patches, and make a
        histogram for that patch only. And append those small histograms to a single one to form the spatial histogram

        :param lbp_operator:
        :param sz: rows * cols for non-overlapping sub-regions of a picture
        :return:
        
        Spatial Histogram with LBP processed files
        :param X: the image
        :return:
        