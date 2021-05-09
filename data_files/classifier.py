from facerec_py.facerec.distance import EuclideanDistance
from facerec_py.facerec.normalization import gaussian_kernel, inverse_dissim
from facerec_py.facerec.util import asRowMatrix
import logging
import numpy as np
import operator as op


class AbstractClassifier(object):
    def compute(self, X, y):
        raise NotImplementedError("E"v"e"r"y" "A"b"s"t"r"a"c"t"C"l"a"s"s"i"f"i"e"r" "m"u"s"t" "i"m"p"l"e"m"e"n"t" "t"h"e" "c"o"m"p"u"t"e" "m"e"t"h"o"d"."")""
""
"" "" "" "" ""d""e""f"" ""p""r""e""d""i""c""t""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""N""o""t""I""m""p""l""e""m""e""n""t""e""d""E""r""r""o""r""(

        :param q: feature
        :param lbl: the specified class label
        :return conf: confidence interval [0, 1]
        :raise NotImplementedError:
        
    Implements a k-Nearest Neighbor Model with a generic distance metric.
    
        Updates the classifier.
        
        Predicts the k-nearest neighbor for a given query in q. 
        
        Args:
        
            q: The given query sample, which is an array.
            
        Returns:
        
            A list with the classifier output. In this framework it is
            assumed, that the predicted class is always returned as first
            element. Moreover, this class returns the distances for the 
            first k-Nearest Neighbors. 
            
            Example:
            
                [ 0, 
                   { 'labels'    : [ 0,      0,      1      ],
                     'distances' : [ 10.132, 10.341, 13.314 ]
                   }
                ]
            
            So if you want to perform a thresholding operation, you could 
            pick the distances in the second array of the generic classifier
            output.    
                    
        
    This class is just a simple wrapper to use libsvm in the 
    CrossValidation module. If you don't use this framework
    use the validation methods coming with LibSVM, they are
    much easier to access (simply pass the correct class 
    labels in svm_predict and you are done...).

    The grid search method in this class is somewhat similar
    to libsvm grid.py, as it performs a parameter search over
    a logarithmic scale.    Again if you don't use this framework, 
    use the libsvm tools as they are much easier to access.

    Please keep in mind to normalize your input data, as expected
    for the model. There's no way to assume a generic normalization
    step.
    
        
        Args:
        
            X: The query image, which is an array.
        
        Returns:
        
            A list with the classifier output. In this framework it is
            assumed, that the predicted class is always returned as first
            element. Moreover, this class returns the libsvm output for
            p_labels, p_acc and p_vals. The libsvm help states:
            
                p_labels: a list of predicted labels
                p_acc: a tuple including  accuracy (for classification), mean-squared 
                   error, and squared correlation coefficient (for regression).
                p_vals: a list of decision values or probability estimates (if '-b 1' 
                    is specified). If k is the number of classes, for decision values,
                    each element includes results of predicting k(k-1)/2 binary-class
                    SVMs. For probabilities, each element contains k values indicating
                    the probability that the testing instance is in each class.
                    Note that the order of classes here is the same as 'model.label'
                    field in the model structure.
        