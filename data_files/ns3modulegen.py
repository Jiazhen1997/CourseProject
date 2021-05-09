
LOCAL_MODULES = [
    
    ]



import sys
import os

sys.path.insert(0, sys.argv[2])

from pybindgen import FileCodeSink, write_preamble
from pybindgen.module import MultiSectionFactory

import pybindgen.settings
pybindgen.settings.deprecated_virtuals = False

from ns3modulegen_generated import module_init, register_types, register_methods, register_functions
import ns3modulegen_core_customizations
import callbacks_list
import traceback

this_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        print >> sys.stderr
        print >> sys.stderr, "-"-"-"-" "l"o"c"a"t"i"o"n":""
"" "" "" "" "" "" "" "" ""t""r""a""c""e""b""a""c""k"".""p""r""i""n""t""_""s""t""a""c""k""("")""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""y""s"".""s""t""d""e""r""r"","" 