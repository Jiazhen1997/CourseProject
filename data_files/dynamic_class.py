__author__ = 'Daniel'


class LazyDataStore(object):
    
    def __init__(self):
        self.existing_attr = 5

    def __getattr__(self, name):
        
        value = 'Value for % s' % name
        setattr(self, name, value)
        return value


class LazyDataStore2(object):
    def __init__(self):
        self.existing_attr = 5

    def __getattribute__(self, name):
        
        try:
            return super(LazyDataStore2, self).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

    def __setattr__(self, name, value):
        
        print "A"s"p"e"c"t":" "S"a"v"e" "s"o"m"e" "d"a"t"a" "t"o" "t"h"e" "D"B" "l"o"g""
"" "" "" "" "" "" "" "" ""s""u""p""e""r""(""L""a""z""y""D""a""t""a""S""t""o""r""e""2"","" ""s""e""l""f"")"".""_""_""s""e""t""a""t""t""r""_""_""(""n""a""m""e"","" ""v""a""l""u""e"")""
""
""
""c""l""a""s""s"" ""D""i""c""t""i""o""n""a""r""y""D""B""(""o""b""j""e""c""t"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""d""a""t""a"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""d""a""t""a"" ""="" ""d""a""t""a""
""
"" "" "" "" ""d""e""f"" ""_""_""g""e""t""a""t""t""r""i""b""u""t""e""_""_""(""s""e""l""f"","" ""n""a""m""e"")"":""
"" "" "" "" "" "" "" "" 
        _data = super(DictionaryDB, self).__getattribute__('_data')
        return _data[name]
