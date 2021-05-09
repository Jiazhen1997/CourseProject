from facerec_py.facerec.feature import AbstractFeature
import numpy as np


class FeatureOperator(AbstractFeature):
    

    def __init__(self, model1, model2):
        if (not isinstance(model1, AbstractFeature)) or (not isinstance(model2, AbstractFeature)):
            raise Exception("A" "F"e"a"t"u"r"e"O"p"e"r"a"t"o"r" "o"n"l"y" "w"o"r"k"s" "o"n" "c"l"a"s"s"e"s" "i"m"p"l"e"m"e"n"t"i"n"g" "a"n" "A"b"s"t"r"a"c"t"F"e"a"t"u"r"e"!"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""o""d""e""l""1"" ""="" ""m""o""d""e""l""1""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""o""d""e""l""2"" ""="" ""m""o""d""e""l""2""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 
    The ChainOperator chains two feature extraction modules:
        model2.compute(model1.compute(X,y),y)
    Where X can be generic input data.
    
    Args:
        model1 [AbstractFeature]
        model2 [AbstractFeature]
    
    The CombineOperator combines the output of two feature extraction modules as:
      (model1.compute(X,y),model2.compute(X,y))
    , where    the output of each feature is a [1xN] or [Nx1] feature vector.
        
        
    Args:
        model1 [AbstractFeature]
        model2 [AbstractFeature]
        
    
    The CombineOperator combines the output of two multidimensional feature extraction modules.
        (model1.compute(X,y),model2.compute(X,y))
        
    Args:
        model1 [AbstractFeature]
        model2 [AbstractFeature]
        hstack [bool] stacks data horizontally if True and vertically if False
        
    