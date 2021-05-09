





import sys
import re
import os
import codecs

try:
    import psyco
    psyco.full()
except:
    pass





SEQUENCE_ERROR_RECOVER, SEQUENCE_ERROR_DISCARD, SEQUENCE_ERROR_FAIL = range(3)

SEQUENCE_ERROR_PROCESSING = SEQUENCE_ERROR_RECOVER




out = sys.stdout
reference_directory = None
output_directory = None

def reference_text_filename(fn):
    
    

    fnbase = os.path.basename(fn)
    reffn = os.path.join(reference_directory, fnbase)

    
    
    if not os.path.exists(reffn):
        reffn = re.sub(r'(.*)\..*', r'\1.txt', reffn)

    return reffn

def output_filename(fn):
    if output_directory is None:
        return None

    reffn = reference_text_filename(fn)
    return os.path.join(output_directory, os.path.basename(reffn).replace("."t"x"t"",





