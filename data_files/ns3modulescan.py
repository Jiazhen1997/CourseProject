

import sys
import os.path

import pybindgen.settings
from pybindgen.gccxmlparser import ModuleParser, PygenClassifier, PygenSection, WrapperWarning
from pybindgen.typehandlers.codesink import FileCodeSink
from pygccxml.declarations import templates
from pygccxml.declarations.class_declaration import class_t
from pygccxml.declarations.calldef import free_function_t, member_function_t, constructor_t, calldef_t




import ns3modulegen_core_customizations




class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, dummy_wrapper, dummy_exception, dummy_traceback_):
        return True
pybindgen.settings.error_handler = ErrorHandler()
import warnings
warnings.filterwarnings(category=WrapperWarning, action='ignore')

type_annotations = {
    '::ns3::AttributeChecker': {
        'automatic_type_narrowing': 'true',
        'allow_subclassing': 'false',
        },
    '::ns3::AttributeValue': {
        'automatic_type_narrowing': 'true',
        'allow_subclassing': 'false',
        },

    '::ns3::CommandLine': {
        'allow_subclassing': 'true', 
        },

    '::ns3::NscTcpL4Protocol': {
        'ignore': 'true', 
        },


    'ns3::RandomVariable::RandomVariable(ns3::RandomVariableBase const & variable) [constructor]': {
        'ignore': None,
        },
    'ns3::RandomVariableBase * ns3::RandomVariable::Peek() const [member function]': {
        'ignore': None,
        },
    'void ns3::RandomVariable::GetSeed(uint32_t * seed) const [member function]': {
        'params': {'seed':{'direction':'out',
                           'array_length':'6'}}
        },
    'bool ns3::TypeId::LookupAttributeByName(std::string name, ns3::TypeId::AttributeInfo * info) const [member function]': {
        'params': {'info':{'transfer_ownership': 'false'}}
        },
    'static bool ns3::TypeId::LookupByNameFailSafe(std::string name, ns3::TypeId * tid) [member function]': {
        'ignore': None, 
        },
    'bool ns3::TraceSourceAccessor::ConnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]': {
        'params': {'obj': {'transfer_ownership':'false'}}
        },
    'bool ns3::TraceSourceAccessor::Connect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]': {
        'params': {'obj': {'transfer_ownership':'false'}}
        },
    'bool ns3::TraceSourceAccessor::DisconnectWithoutContext(ns3::ObjectBase * obj, ns3::CallbackBase const & cb) const [member function]': {
        'params': {'obj': {'transfer_ownership':'false'}}
        },
    'bool ns3::TraceSourceAccessor::Disconnect(ns3::ObjectBase * obj, std::string context, ns3::CallbackBase const & cb) const [member function]': {
        'params': {'obj': {'transfer_ownership':'false'}}
        },
    'bool ns3::AttributeAccessor::Set(ns3::ObjectBase * object, ns3::AttributeValue const & value) const [member function]': {
        'params': {'object': {'transfer_ownership':'false'}}
        },
    'ns3::EmpiricalVariable::EmpiricalVariable(ns3::RandomVariableBase const & variable) [constructor]': {
        'ignore': None
        },
    'static ns3::AttributeList * ns3::AttributeList::GetGlobal() [member function]': {
        'caller_owns_return': 'false'
        },
    'void ns3::CommandLine::Parse(int argc, char * * argv) const [member function]': {
        'ignore': None 
        },
    'extern void ns3::PythonCompleteConstruct(ns3::Ptr<ns3::Object> object, ns3::TypeId typeId, ns3::AttributeList const & attributes) [free function]': {
        'ignore': None 
        },

    'ns3::Ptr<ns3::Ipv4RoutingProtocol> ns3::Ipv4ListRouting::GetRoutingProtocol(uint32_t index, int16_t & priority) const [member function]': {
        'params': {'priority':{'direction':'out'}}
        },
    'ns3::Ipv4RoutingTableEntry * ns3::GlobalRouter::GetInjectedRoute(uint32_t i) [member function]': {
        'params': {'return': { 'caller_owns_return': 'false',}},
        },
    'ns3::Ipv4RoutingTableEntry * ns3::Ipv4GlobalRouting::GetRoute(uint32_t i) const [member function]': {
        'params': {'return': { 'caller_owns_return': 'false',}},
        },

    '::ns3::TestCase': {
        'ignore': 'true', 
        },
    '::ns3::TestRunner': {
        'ignore': 'true', 
        },
    '::ns3::TestSuite': {
        'ignore': 'true', 
        },
    
    }

def get_ns3_relative_path(path):
    l = []
    head = path
    while head:
        head, tail = os.path.split(head)
        if tail == 'ns3':
            return os.path.join(*l)
        l.insert(0, tail)
    raise AssertionError("i"s" "t"h"e" "p"a"t"h" "%"r" "i"n"s"i"d"e" "n"s"3"?"!"" ""%"" ""p""a""t""h"")""
""
""
""d""e""f"" ""p""r""e""_""s""c""a""n""_""h""o""o""k""(""d""u""m""m""y""_""m""o""d""u""l""e""_""p""a""r""s""e""r"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""y""g""c""c""x""m""l""_""d""e""f""i""n""i""t""i""o""n"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""g""l""o""b""a""l""_""a""n""n""o""t""a""t""i""o""n""s"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""a""r""a""m""e""t""e""r""_""a""n""n""o""t""a""t""i""o""n""s"")"":""
"" "" "" "" ""n""s""3""_""h""e""a""d""e""r"" ""="" ""g""e""t""_""n""s""3""_""r""e""l""a""t""i""v""e""_""p""a""t""h""(""p""y""g""c""c""x""m""l""_""d""e""f""i""n""i""t""i""o""n"".""l""o""c""a""t""i""o""n"".""f""i""l""e""_""n""a""m""e"")""
""
"" "" "" "" ""#""#"" ""N""o""t""e"":"" ""w""e"" ""d""o""n""'""t"" ""i""n""c""l""u""d""e"" ""l""i""n""e"" ""n""u""m""b""e""r""s"" ""i""n"" ""t""h""e"" ""c""o""m""m""e""n""t""s"" ""b""e""c""a""u""s""e""
"" "" "" "" ""#""#"" ""t""h""o""s""e"" ""n""u""m""b""e""r""s"" ""a""r""e"" ""v""e""r""y"" ""l""i""k""e""l""y"" ""t""o"" ""c""h""a""n""g""e"" ""f""r""e""q""u""e""n""t""l""y"","" ""w""h""i""c""h"" ""w""o""u""l""d""
"" "" "" "" ""#""#"" ""c""a""u""s""e"" ""n""e""e""d""l""e""s""s"" ""c""h""a""n""g""e""s"","" ""s""i""n""c""e"" ""t""h""e"" ""g""e""n""e""r""a""t""e""d"" ""p""y""t""h""o""n"" ""f""i""l""e""s"" ""a""r""e""
"" "" "" "" ""#""#"" ""k""e""p""t"" ""u""n""d""e""r"" ""v""e""r""s""i""o""n"" ""c""o""n""t""r""o""l"".""
""
"" "" "" "" ""#""g""l""o""b""a""l""_""a""n""n""o""t""a""t""i""o""n""s""[""'""p""y""g""e""n""_""c""o""m""m""e""n""t""'""]"" ""="" 