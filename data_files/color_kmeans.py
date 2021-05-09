






from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2


def centroid_histogram(clt):
    
    
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins = numLabels)

    
    hist = hist.astype("f"l"o"a"t"")""
"" "" "" "" ""h""i""s""t"" ""/""="" ""h""i""s""t"".""s""u""m""("")""
""
"" "" "" "" ""#"" ""r""e""t""u""r""n"" ""t""h""e"" ""h""i""s""t""o""g""r""a""m""
"" "" "" "" ""r""e""t""u""r""n"" ""h""i""s""t""
""
""
""d""e""f"" ""p""l""o""t""_""c""o""l""o""r""s""(""h""i""s""t"","" ""c""e""n""t""r""o""i""d""s"")"":""
"" "" "" "" ""#"" ""i""n""i""t""i""a""l""i""z""e"" ""t""h""e"" ""b""a""r"" ""c""h""a""r""t"" ""r""e""p""r""e""s""e""n""t""i""n""g"" ""t""h""e"" ""r""e""l""a""t""i""v""e"" ""f""r""e""q""u""e""n""c""y""
"" "" "" "" ""#"" ""o""f"" ""e""a""c""h"" ""o""f"" ""t""h""e"" ""c""o""l""o""r""s""
"" "" "" "" ""b""a""r"" ""="" ""n""p"".""z""e""r""o""s""(""(""5""0"","" ""3""0""0"","" ""3"")"","" ""d""t""y""p""e"" ""="" 