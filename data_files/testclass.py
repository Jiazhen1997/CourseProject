__author__ = 'Daniel'


def _add_tests(generator):
    
    def class_decorator(cls):
        
        for f, args in generator():
            
            test = lambda self, args=args, f=f: f(self, *args)

            test.__name__ = "t"e"s"t"_"%"s"_"%"s"" ""%"" ""(""f"".""_""_""n""a""m""e""_""_"","" ""a""r""g""s""[""0""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""t""a""t""t""r""(""c""l""s"","" ""t""e""s""t"".""_""_""n""a""m""e""_""_"","" ""t""e""s""t"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""c""l""s""
""
"" "" "" "" ""r""e""t""u""r""n"" ""c""l""a""s""s""_""d""e""c""o""r""a""t""o""r