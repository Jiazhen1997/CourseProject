import re

from pybindgen.typehandlers import base as typehandlers
from pybindgen import ReturnValue, Parameter
from pybindgen.cppmethod import CustomCppMethodWrapper, CustomCppConstructorWrapper
from pybindgen.typehandlers.codesink import MemoryCodeSink
from pybindgen.typehandlers import ctypeparser
from pybindgen import cppclass
import warnings

from pybindgen.typehandlers.base import CodeGenerationError

import sys

class SmartPointerTransformation(typehandlers.TypeTransformation):
    
    def __init__(self):
        super(SmartPointerTransformation, self).__init__()
        self.rx = re.compile(r'(ns3::|::ns3::|)Ptr<([^>]+)>\s*$')

    def _get_untransformed_type_traits(self, name):
        m = self.rx.match(name)
        is_const = False
        if m is None:
            return None, False
        else:
            name1 = m.group(2).strip()
            if name1.startswith('const '):
                name1 = name1[len('const '):]
                is_const = True
            if name1.endswith(' const'):
                name1 = name1[:-len(' const')]
                is_const = True
            new_name = name1+' *'

            if new_name.startswith('::'):
                new_name = new_name[2:]
            return new_name, is_const

    def get_untransformed_name(self, name):
        new_name, dummy_is_const = self._get_untransformed_type_traits(name)
        return new_name

    def create_type_handler(self, type_handler, *args, **kwargs):
        if issubclass(type_handler, Parameter):
            kwargs['transfer_ownership'] = False
        elif issubclass(type_handler, ReturnValue):
            kwargs['caller_owns_return'] = False
        else:
            raise AssertionError

        
        orig_ctype, is_const = self._get_untransformed_type_traits(args[0])
        if is_const:
            correct_ctype = 'ns3::Ptr< %s const >' % orig_ctype[:-2]
        else:
            correct_ctype = 'ns3::Ptr< %s >' % orig_ctype[:-2]
        args = tuple([correct_ctype] + list(args[1:]))

        handler = type_handler(*args, **kwargs)
        handler.set_tranformation(self, orig_ctype)
        return handler

    def untransform(self, type_handler, declarations, code_block, expression):
        return 'const_cast<%s> (ns3::PeekPointer (%s))' % (type_handler.untransformed_ctype, expression)

    def transform(self, type_handler, declarations, code_block, expression):
        assert type_handler.untransformed_ctype[-1] == '*'
        return 'ns3::Ptr< %s > (%s)' % (type_handler.untransformed_ctype[:-1], expression)


transf = SmartPointerTransformation()
typehandlers.return_type_matcher.register_transformation(transf)
typehandlers.param_type_matcher.register_transformation(transf)
del transf


class ArgvParam(Parameter):
    

    DIRECTIONS = [Parameter.DIRECTION_IN]
    CTYPES = []
    
    def convert_c_to_python(self, wrapper):
        raise NotImplementedError

    def convert_python_to_c(self, wrapper):
        py_name = wrapper.declarations.declare_variable('PyObject*', 'py_' + self.name)
        argc_var = wrapper.declarations.declare_variable('int', 'argc')
        name = wrapper.declarations.declare_variable('char**', self.name)
        idx = wrapper.declarations.declare_variable('Py_ssize_t', 'idx')
        wrapper.parse_params.add_parameter('O!', ['&PyList_Type', '&'+py_name], self.name)

        

        wrapper.before_call.write_code("%"s" "=" "("c"h"a"r" "*"*")" "m"a"l"l"o"c"("s"i"z"e"o"f"("c"h"a"r"*")"*"P"y"L"i"s"t"_"S"i"z"e"("%"s")")";""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""%"" ""(""n""a""m""e"","" ""p""y""_""n""a""m""e"")"")""
"" "" "" "" "" "" "" "" ""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""a""d""d""_""c""l""e""a""n""u""p""_""c""o""d""e""(""'""f""r""e""e""(""%""s"")"";""'"" ""%"" ""n""a""m""e"")""
"" "" "" "" "" "" "" "" ""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""w""r""i""t""e""_""c""o""d""e""(""'""'""'""
""f""o""r"" ""(""%""(""i""d""x"")""s"" ""="" ""0"";"" ""%""(""i""d""x"")""s"" ""<"" ""P""y""L""i""s""t""_""S""i""z""e""(""%""(""p""y""_""n""a""m""e"")""s"")"";"" ""%""(""i""d""x"")""s""+""+"")""
""{""
""'""'""'"" ""%"" ""v""a""r""s""("")"")""
"" "" "" "" "" "" "" "" ""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""s""i""n""k"".""i""n""d""e""n""t""("")""
"" "" "" "" "" "" "" "" ""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""w""r""i""t""e""_""c""o""d""e""(""'""'""'""
""P""y""O""b""j""e""c""t"" ""*""i""t""e""m"" ""="" ""P""y""L""i""s""t""_""G""E""T""_""I""T""E""M""(""%""(""p""y""_""n""a""m""e"")""s"","" ""%""(""i""d""x"")""s"")"";""
""'""'""'"" ""%"" ""v""a""r""s""("")"")""
"" "" "" "" "" "" "" "" ""#""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""w""r""i""t""e""_""e""r""r""o""r""_""c""h""e""c""k""(""'""i""t""e""m"" ""=""="" ""N""U""L""L""'"")""
"" "" "" "" "" "" "" "" ""w""r""a""p""p""e""r"".""b""e""f""o""r""e""_""c""a""l""l"".""w""r""i""t""e""_""e""r""r""o""r""_""c""h""e""c""k""(""
"" "" "" "" "" "" "" "" "" "" "" "" ""'""!""P""y""S""t""r""i""n""g""_""C""h""e""c""k""(""i""t""e""m"")""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""a""i""l""u""r""e""_""c""l""e""a""n""u""p""=""(""'""P""y""E""r""r""_""S""e""t""S""t""r""i""n""g""(""P""y""E""x""c""_""T""y""p""e""E""r""r""o""r"","" ""'""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'
    Class that generates a proxy virtual method that calls a similarly named python method.
    code to call the python method
static ns3::TypeId GetTypeId (void)
{
  static ns3::TypeId tid = ns3::TypeId ("%"s"")""
"" "" "" "" "".""S""e""t""P""a""r""e""n""t""<"" ""%""s"" "">"" ""("")""
"" "" "" "" "";""
"" "" ""r""e""t""u""r""n"" ""t""i""d"";""
""}