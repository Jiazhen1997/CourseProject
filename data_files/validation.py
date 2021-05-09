from __future__ import absolute_import
import math as math
import random as random
import logging
import cv2

import numpy as np

from facerec_py.facerec.model import PredictableModel, AbstractPredictableModel
from util.commons_util.fundamentals.generators import frange















class TFPN(object):
    def __init__(self, TP=0, FP=0, TN=0, FN=0):
        self.rates = np.array([TP, FP, TN, FN], dtype=np.double)

    @property
    def TP(self):
        return self.rates[0]

    @TP.setter
    def TP(self, value):
        self.rates[0] = value

    @property
    def FP(self):
        return self.rates[1]

    @FP.setter
    def FP(self, value):
        self.rates[1] = value

    @property
    def TN(self):
        return self.rates[2]

    @TN.setter
    def TN(self, value):
        self.rates[2] = value

    @property
    def FN(self):
        return self.rates[3]

    @FN.setter
    def FN(self, value):
        self.rates[3] = value

    def __add__(self, other):
        return self.rates + other.rates

    def __iadd__(self, other):
        self.rates += other.rates
        return self


def shuffle(X, y):
    
    idx = np.argsort([random.random() for _ in xrange(len(y))])  
    X = [X[i] for i in idx]
    y = y[idx]
    return X, y


def slice_2d(X, rows, cols):
    
    return [X[i][j] for j in cols for i in rows]


def precision(true_positives, false_positives):
    
    return accuracy(true_positives, 0, false_positives, 0)


def accuracy(true_positives, true_negatives, false_positives, false_negatives, description=None):
    
    true_positives = float(true_positives)
    true_negatives = float(true_negatives)
    false_positives = float(false_positives)
    false_negatives = float(false_negatives)
    if (true_positives + true_negatives + false_positives + false_negatives) < 1e-15:
        return 0.0
    return (true_positives + true_negatives) / (true_positives + false_positives + true_negatives + false_negatives)


class ValidationResult(object):
    

    def __init__(self, true_positives, true_negatives, false_positives, false_negatives, description):
        self.true_positives = true_positives
        self.true_negatives = true_negatives
        self.false_positives = false_positives
        self.false_negatives = false_negatives
        self.description = description

    def __div(self, x, y):
        
        if y < 1e-15:
            return 0.0
        return x/y

    @property
    def TPR(self):
        return self.__div(self.true_positives, self.true_positives+self.false_negatives)

    @property
    def FPR(self):
        return self.__div(self.false_positives, self.false_positives+self.true_negatives)

    @property
    def recall(self):
        return self.__div(self.true_positives, self.true_positives+self.false_negatives)

    @property
    def precision(self):
        return self.__div(self.true_positives, self.true_positives+self.false_positives)

    @property
    def total(self):
        return self.true_negatives+self.true_positives+self.false_negatives+self.false_positives
    @property
    def accuracy(self):
        return self.__div(self.true_positives+self.true_negatives, self.total)

    @property
    def F1(self):
        return self.__div(2*self.precision*self.recall, self.precision+self.recall)

    def __repr__(self):
        return "V"a"l"i"d"a"t"i"o"n"R"e"s"u"l"t" "("D"e"s"c"r"i"p"t"i"o"n"="%"s"," "P"r"e"c"i"s"i"o"n"="%"."2"f"%"%"," "R"e"c"a"l"l"="%"."2"f"%"%"," "T"P"R"="%"."2"f"%"%"," "F"P"R"="%"."2"f"%"%"," "T"P"="%"d"," "T"N"="%"d"," "F"P"="%"d"," "F"N"="%"d")"" ""%"" ""(""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""e""s""c""r""i""p""t""i""o""n"","" ""s""e""l""f"".""p""r""e""c""i""s""i""o""n""*""1""0""0"","" ""s""e""l""f"".""r""e""c""a""l""l""*""1""0""0"","" ""s""e""l""f"".""T""P""R""*""1""0""0"","" ""s""e""l""f"".""F""P""R""*""1""0""0"","" ""s""e""l""f"".""t""r""u""e""_""p""o""s""i""t""i""v""e""s"","" ""s""e""l""f"".""t""r""u""e""_""n""e""g""a""t""i""v""e""s"","" ""s""e""l""f"".""f""a""l""s""e""_""p""o""s""i""t""i""v""e""s"","" ""s""e""l""f"".""f""a""l""s""e""_""n""e""g""a""t""i""v""e""s"")""
""
""
""c""l""a""s""s"" ""V""a""l""i""d""a""t""i""o""n""S""t""r""a""t""e""g""y""(""o""b""j""e""c""t"")"":""
"" "" "" "" 

    def __init__(self, model):
        
        if not isinstance(model, AbstractPredictableModel):
            raise TypeError("V"a"l"i"d"a"t"i"o"n" "c"a"n" "o"n"l"y" "v"a"l"i"d"a"t"e" "t"h"e" "t"y"p"e" "P"r"e"d"i"c"t"a"b"l"e"M"o"d"e"l"."")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""o""d""e""l"" ""="" ""m""o""d""e""l""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t""s"" ""="" ""[""]""
""
"" "" "" "" ""d""e""f"" ""a""d""d""(""s""e""l""f"","" ""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t""s"".""a""p""p""e""n""d""(""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t"")""
""
"" "" "" "" ""d""e""f"" ""v""a""l""i""d""a""t""e""(""s""e""l""f"","" ""X"","" ""y"","" ""d""e""s""c""r""i""p""t""i""o""n"")"":""
"" "" "" "" "" "" "" "" 
        raise NotImplementedError("E"v"e"r"y" "V"a"l"i"d"a"t"i"o"n" "m"o"d"u"l"e" "m"u"s"t" "i"m"p"l"e"m"e"n"t" "t"h"e" "v"a"l"i"d"a"t"e" "m"e"t"h"o"d"!"")""
""
"" "" "" "" ""d""e""f"" ""p""r""i""n""t""_""r""e""s""u""l""t""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""s""e""l""f"".""m""o""d""e""l""
"" "" "" "" "" "" "" "" ""f""o""r"" ""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t"" ""i""n"" ""s""e""l""f"".""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""v""a""l""i""d""a""t""i""o""n""_""r""e""s""u""l""t""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n""  
    
    Divides the Data into 10 equally spaced and non-overlapping folds for training and testing.
    
    Here is a 3-fold cross validation example for 9 observations and 3 classes, so each observation is given by its index [c_i][o_i]:
                
        o0 o1 o2        o0 o1 o2        o0 o1 o2  
    c0 | A  B  B |  c0 | B  A  B |  c0 | B  B  A |
    c1 | A  B  B |  c1 | B  A  B |  c1 | B  B  A |
    c2 | A  B  B |  c2 | B  A  B |  c2 | B  B  A |
    
    Please note: If there are less than k observations in a class, k is set to the minimum of observations available through all classes.
    

        :param model:
        :param k: [int] number of folds in this k-fold cross-validation (default 10)
        :param threshold_up: threshold upper limit for ROC curve, range [0, 1]; 0 to disable ROC
        :return:
        
        X, y are original data
        :param X: X [dim x num_data] input data to validate on
        :param y: y [1 x num_data] classes
        :param description:
        :return:
        
        display the gray scale image
        :param data: matrix
        :param actual: actual label
        :param predicted: predicted label
        :return:
        
        Binary classification thresholding strategy
        :param testIdX:
        :param predictions:
        :param y:
        :param threshold:
        :return:
         Leave-One-Cross Validation (LOOCV) uses one observation for testing and the rest for training a classifier:

        o0 o1 o2        o0 o1 o2        o0 o1 o2           o0 o1 o2
    c0 | A  B  B |  c0 | B  A  B |  c0 | B  B  A |     c0 | B  B  B |
    c1 | B  B  B |  c1 | B  B  B |  c1 | B  B  B |     c1 | B  B  B |
    c2 | B  B  B |  c2 | B  B  B |  c2 | B  B  B | ... c2 | B  B  A |
    
    Arguments:
        model [Model] model for this validation
        ... see [Validation]
     Intialize Cross-Validation module.
        
        Args:
            model [Model] model for this validation
         Performs a LOOCV.
        
        Args:
            X [dim x num_data] input data to validate on
            y [1 x num_data] classes
         Leave-One-Cross Validation (LOOCV) uses one observation for testing and the rest for training a classifier:

        o0 o1 o2        o0 o1 o2        o0 o1 o2           o0 o1 o2
    c0 | A  B  B |  c0 | B  A  B |  c0 | B  B  A |     c0 | B  B  B |
    c1 | B  B  B |  c1 | B  B  B |  c1 | B  B  B |     c1 | B  B  B |
    c2 | B  B  B |  c2 | B  B  B |  c2 | B  B  B | ... c2 | B  B  A |
    
    Arguments:
        model [Model] model for this validation
        ... see [Validation]
     Intialize Cross-Validation module.
        
        Args:
            model [Model] model for this validation
        
        TODO Add example and refactor into proper interface declaration.
        Implements a simple Validation, which allows you to partition the data yourself.
    
        Args:
            model [PredictableModel] model to perform the validation on
        

        Performs a validation given training data and test data. User is responsible for non-overlapping assignment of indices.

        Args:
            X [dim x num_data] input data to validate on
            y [1 x num_data] classes
        