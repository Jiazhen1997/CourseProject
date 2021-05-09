import sys
import os

import numpy as np
from PIL import Image
import re

__author__ = 'Danyang'


def read_images(path, sz=None):
    
    c = 0
    X, y = [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if not re.search(r"\"."p"g"m"$"|"\"."j"p"g"$"","" ""f""i""l""e""n""a""m""e"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r""e"".""s""e""a""r""c""h""(""r