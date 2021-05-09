

import os

from LBP import *
import cv2
import pickle
from util.commons_util.logger_utils.Timer import Timer
from multiprocessing import Pool


radius = 1

nei = 8

scale = 4

scale_step = 1.25

winsize = int((25 - 1) / 2)

stride = 2



orl_path = 'E:/GPforFR/data/orl_faces'
lfw_path = 'E:/GPforFR/data/lfw_p'


orl_dst_path = 'E:/GPforFR/data/orl_faces_feature'
lfw_dst_path = 'E:/GPforFR/data/lfw_feature'

def extract_feature(args):
    timer = Timer()
    timer.start()

    img_path, ftr_name = args
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if not os.path.exists(os.path.dirname(ftr_name)):
        os.makedirs(os.path.dirname(ftr_name))
    out_file = open(ftr_name, 'w')
    feature = multi_scale_lbp_feature(image, radius, nei, scale, scale_step, winsize, stride)
    pickle.dump(feature, out_file)
    out_file.close()

    print timer.end()


def extract(dir_path, dst_path, include_folder_name=False):
    
    p = Pool(4)
    for root, dirs, files in os.walk(dir_path):
        if files:
            load = []
            for f in files:
                img_path = root + '/' + f
                folder = "" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""i""n""c""l""u""d""e""_""f""o""l""d""e""r""_""n""a""m""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""l""d""e""r"" ""="" ""r""o""o""t"".""r""e""p""l""a""c""e""(""'""/""'"","" ""'""/""'"")"".""s""p""l""i""t""(""'""/""'"")""[""-""1""]""+""'""_""'""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""t""r""_""n""a""m""e"" ""="" ""o""s"".""p""a""t""h"".""j""o""i""n""(""d""s""t""_""p""a""t""h"","" ""f""o""l""d""e""r""+""f"".""s""p""l""i""t""(""'"".""'"")""[""0""]"" ""+"" ""'"".""t""x""t""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""o""a""d"".""a""p""p""e""n""d""(""(""i""m""g""_""p""a""t""h"","" ""f""t""r""_""n""a""m""e"")"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""p"".""m""a""p""(""e""x""t""r""a""c""t""_""f""e""a""t""u""r""e"","" ""l""o""a""d"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""e""x""t""r""a""c""t""_""f""e""a""t""u""r""e""(""l""o""a""d""[""0""]"")""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""r""o""o""t""
"" "" "" "" ""p"".""c""l""o""s""e""("")""
""
""i""f"" ""_""_""n""a""m""e""_""_""=""=