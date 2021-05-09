













from __future__ import with_statement

import sys
import re
try:
    import annotation
except ImportError:
    import os.path
    from sys import path as sys_path
    
    sys_path.append(os.path.join(os.path.dirname(__file__), '../server/src'))
    import annotation


sys_path.append(os.path.join(os.path.dirname(__file__), '..'))
    
options = None

def ent2event(anntype, fn):
    global options

    mapped = 0

    try:
        
        nosuff_fn = fn.replace("."a"n"n"",