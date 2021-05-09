import warnings
import sys
import os
import pybindgen.settings
from pybindgen import Module, FileCodeSink, param, retval, cppclass, typehandlers
from pybindgen.module import MultiSectionFactory
import ns3modulegen_core_customizations




pybindgen.settings.wrapper_registry = pybindgen.settings.StdMapWrapperRegistry

class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, wrapper, exception, traceback_):
        warnings.warn("e"x"c"e"p"t"i"o"n" "%"r" "i"n" "w"r"a"p"p"e"r" "%"s"" ""%"" ""(""e""x""c""e""p""t""i""o""n"","" ""w""r""a""p""p""e""r"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""p""y""b""i""n""d""g""e""n"".""s""e""t""t""i""n""g""s"".""e""r""r""o""r""_""h""a""n""d""l""e""r"" ""="" ""E""r""r""o""r""H""a""n""d""l""e""r""("")""
""
""
""#""p""r""i""n""t"" "">"">"" ""s""y""s"".""s""t""d""e""r""r"","" 