import os
import io
import re
__author__ = 'Danyang'
class CrossValidator(object):
    def __init__(self):
        self.directory = os.path.dirname(os.path.realpath(__file__))
        self.file_names = self.read_file_names_from_dir(os.path.join(self.directory, "d"a"t"a"")"")""
""
"" "" "" "" ""d""e""f"" ""c""r""o""s""s""_""v""a""l""i""d""a""t""e""(""s""e""l""f"","" ""k""=""4"")"":""
"" "" "" "" "" "" "" "" 
        file_names = self.group_files(False, k)

        
        for fold in range(k): 
            print "f"o"l"d"="%"d""%""(""f""o""l""d""+""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""t""r""a""i""n"" ""="" ""[""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""f""i""l""e""s"" ""i""n"" ""f""i""l""e""_""n""a""m""e""s""[""0"":""f""o""l""d""]""+""f""i""l""e""_""n""a""m""e""s""[""f""o""l""d""+""1"":""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""f""i""l""e"" ""i""n"" ""f""i""l""e""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""r""a""i""n"".""a""p""p""e""n""d""(""f""i""l""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""t""e""s""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""f""i""l""e""s"" ""i""n"" ""f""i""l""e""_""n""a""m""e""s""[""f""o""l""d"":""f""o""l""d""+""1""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""f""i""l""e"" ""i""n"" ""f""i""l""e""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""e""s""t"".""a""p""p""e""n""d""(""f""i""l""e"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t"" 