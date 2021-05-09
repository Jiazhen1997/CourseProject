

import sys
import os.path

import pybindgen.settings
from pybindgen.gccxmlparser import ModuleParser, PygenClassifier, PygenSection, WrapperWarning, find_declaration_from_name
from pybindgen.typehandlers.codesink import FileCodeSink
from pygccxml.declarations import templates
from pygccxml.declarations.enumeration import enumeration_t
from pygccxml.declarations.class_declaration import class_t
from pygccxml.declarations.calldef import free_function_t, member_function_t, constructor_t, calldef_t




import ns3modulegen_core_customizations




class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, dummy_wrapper, dummy_exception, dummy_traceback_):
        return True
pybindgen.settings.error_handler = ErrorHandler()
import warnings
warnings.filterwarnings(category=WrapperWarning, action='ignore')


import ns3modulescan
type_annotations = ns3modulescan.type_annotations


def get_ns3_relative_path(path):
    l = []
    head = path
    while head:
        new_head, tail = os.path.split(head)
        if new_head == head:
            raise ValueError
        head = new_head
        if tail == 'ns3':
            return os.path.join(*l)
        l.insert(0, tail)
    raise AssertionError("i"s" "t"h"e" "p"a"t"h" "%"r" "i"n"s"i"d"e" "n"s"3"?"!"" ""%"" ""p""a""t""h"")""
""
""c""l""a""s""s"" ""P""r""e""S""c""a""n""H""o""o""k"":""
""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""h""e""a""d""e""r""s""_""m""a""p"","" ""m""o""d""u""l""e"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""h""e""a""d""e""r""s""_""m""a""p"" ""="" ""h""e""a""d""e""r""s""_""m""a""p""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""m""o""d""u""l""e"" ""="" ""m""o""d""u""l""e""
""
"" "" "" "" ""d""e""f"" ""_""_""c""a""l""l""_""_""(""s""e""l""f"","" ""m""o""d""u""l""e""_""p""a""r""s""e""r"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""y""g""c""c""x""m""l""_""d""e""f""i""n""i""t""i""o""n"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""g""l""o""b""a""l""_""a""n""n""o""t""a""t""i""o""n""s"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""a""r""a""m""e""t""e""r""_""a""n""n""o""t""a""t""i""o""n""s"")"":""
"" "" "" "" "" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""s""3""_""h""e""a""d""e""r"" ""="" ""g""e""t""_""n""s""3""_""r""e""l""a""t""i""v""e""_""p""a""t""h""(""p""y""g""c""c""x""m""l""_""d""e""f""i""n""i""t""i""o""n"".""l""o""c""a""t""i""o""n"".""f""i""l""e""_""n""a""m""e"")""
"" "" "" "" "" "" "" "" ""e""x""c""e""p""t"" ""V""a""l""u""e""E""r""r""o""r"":"" ""#"" ""t""h""e"" ""h""e""a""d""e""r"" ""i""s"" ""n""o""t"" ""f""r""o""m"" ""n""s""3""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""#"" ""i""g""n""o""r""e"" ""t""h""e"" ""d""e""f""i""n""i""t""i""o""n"","" ""i""t""'""s"" ""n""o""t"" ""n""s""-""3"" ""d""e""f"".""
""
"" "" "" "" "" "" "" "" ""d""e""f""i""n""i""t""i""o""n""_""m""o""d""u""l""e"" ""="" ""s""e""l""f"".""h""e""a""d""e""r""s""_""m""a""p""[""n""s""3""_""h""e""a""d""e""r""]""
""
"" "" "" "" "" "" "" "" ""#""#"" ""N""o""t""e"":"" ""w""e"" ""d""o""n""'""t"" ""i""n""c""l""u""d""e"" ""l""i""n""e"" ""n""u""m""b""e""r""s"" ""i""n"" ""t""h""e"" ""c""o""m""m""e""n""t""s"" ""b""e""c""a""u""s""e""
"" "" "" "" "" "" "" "" ""#""#"" ""t""h""o""s""e"" ""n""u""m""b""e""r""s"" ""a""r""e"" ""v""e""r""y"" ""l""i""k""e""l""y"" ""t""o"" ""c""h""a""n""g""e"" ""f""r""e""q""u""e""n""t""l""y"","" ""w""h""i""c""h"" ""w""o""u""l""d""
"" "" "" "" "" "" "" "" ""#""#"" ""c""a""u""s""e"" ""n""e""e""d""l""e""s""s"" ""c""h""a""n""g""e""s"","" ""s""i""n""c""e"" ""t""h""e"" ""g""e""n""e""r""a""t""e""d"" ""p""y""t""h""o""n"" ""f""i""l""e""s"" ""a""r""e""
"" "" "" "" "" "" "" "" ""#""#"" ""k""e""p""t"" ""u""n""d""e""r"" ""v""e""r""s""i""o""n"" ""c""o""n""t""r""o""l"".""
""
"" "" "" "" "" "" "" "" ""#""g""l""o""b""a""l""_""a""n""n""o""t""a""t""i""o""n""s""[""'""p""y""g""e""n""_""c""o""m""m""e""n""t""'""]"" ""="" 