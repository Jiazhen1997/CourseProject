



from os import listdir
from os.path import isdir, join as path_join
from re import compile as re_compile, match


from pexpect import spawn


SENTENCE_OUTPUT_REGEX = re_compile(r'Sentence 
OUTPUT_TOKEN_REGEX = re_compile(
    r' CharacterOffsetBegin=(?P<start>[0-9]+).*'
    r' CharacterOffsetEnd=(?P<end>[0-9]+).*'
    r' NamedEntityTag=(?P<type>[^ \]]+)'
    )



class CoreNLPTagger(object):
    def __init__(self, core_nlp_path, mem='1024m'):
        assert isdir(core_nlp_path)
        
        jar_paths = []
        for jar_regex in (
                '^stanford-corenlp-[0-9]{4}-[0-9]{2}-[0-9]{2}\.jar$',
                '^stanford-corenlp-[0-9]{4}-[0-9]{2}-[0-9]{2}-models\.jar$',
                '^joda-time\.jar$',
                '^xom\.jar$',
                ):
            for fname in listdir(core_nlp_path):
                if match(jar_regex, fname):
                    jar_paths.append(path_join(core_nlp_path, fname))
                    break
            else:
                assert False, 'could not locate any jar on the form "%"s""'"" ""%"" ""j""a""r""_""r""e""g""e""x""
""
"" "" "" "" "" "" "" "" ""#"" ""T""h""e""n"" ""h""o""o""k"" ""u""p"" ""t""h""e"" ""C""o""r""e""N""L""P"" ""p""r""o""c""e""s""s""
"" "" "" "" "" "" "" "" ""c""o""r""e""n""l""p""_""c""m""d"" ""="" ""'"" ""'"".""j""o""i""n""(""(""'""j""a""v""a"" ""-""X""m""x""%""s""'"" ""%"" ""m""e""m"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""-""c""p"" ""%""s""'"" ""%"" ""'"":""'"".""j""o""i""n""(""j""a""r""_""p""a""t""h""s"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""e""d""u"".""s""t""a""n""f""o""r""d"".""n""l""p"".""p""i""p""e""l""i""n""e"".""S""t""a""n""f""o""r""d""C""o""r""e""N""L""P""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""-""a""n""n""o""t""a""t""o""r""s"" ""t""o""k""e""n""i""z""e"",""s""s""p""l""i""t"",""p""o""s"",""l""e""m""m""a"",""n""e""r""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "")"")""
""
"" "" "" "" "" "" "" "" ""#"" ""S""p""a""w""n"" ""t""h""e"" ""p""r""o""c""e""s""s""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""c""o""r""e""_""n""l""p""_""p""r""o""c""e""s""s"" ""="" ""s""p""a""w""n""(""c""o""r""e""n""l""p""_""c""m""d"","" ""t""i""m""e""o""u""t""=""6""0""0"")""
"" "" "" "" "" "" "" "" ""#"" ""W""a""i""t"" ""f""o""r"" ""t""h""e"" ""m""o""d""e""l""s"" ""t""o"" ""l""o""a""d"","" ""t""h""i""s"" ""i""s"" ""n""o""t"" ""o""v""e""r""l""y"" ""f""a""s""t""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""c""o""r""e""_""n""l""p""_""p""r""o""c""e""s""s"".""e""x""p""e""c""t""(""'""E""n""t""e""r""i""n""g"" ""i""n""t""e""r""a""c""t""i""v""e"" ""s""h""e""l""l"".""'"")""
""
"" "" "" "" ""d""e""f"" ""_""_""d""e""l""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""#"" ""I""f"" ""o""u""r"" ""c""h""i""l""d"" ""p""r""o""c""e""s""s"" ""i""s"" ""s""t""i""l""l"" ""a""r""o""u""n""d"","" ""k""i""l""l"" ""i""t""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""_""c""o""r""e""_""n""l""p""_""p""r""o""c""e""s""s"".""i""s""a""l""i""v""e""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""c""o""r""e""_""n""l""p""_""p""r""o""c""e""s""s"".""t""e""r""m""i""n""a""t""e""("")""
""
"" "" "" "" ""d""e""f"" ""t""a""g""(""s""e""l""f"","" ""t""e""x""t"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""c""o""r""e""_""n""l""p""_""p""r""o""c""e""s""s"".""s""e""n""d""l""i""n""e""(""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""N""e""w""l""i""n""e""s"" ""a""r""e"" ""n""o""t"" ""h""e""a""l""t""h""y"" ""a""t"" ""t""h""i""s"" ""s""t""a""g""e"","" ""r""e""m""o""v""e"" ""t""h""e""m"","" ""t""h""e""y""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" "" "" ""w""o""n""'""t"" ""a""f""f""e""c""t"" ""t""h""e"" ""o""f""f""s""e""t""s""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""e""x""t"".""r""e""p""l""a""c""e""(""'""\""n""'"","" ""'"" ""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "")""
""
"" "" "" "" "" "" "" "" ""#"" ""W""e"" ""c""a""n"" ""e""x""p""e""c""t"" ""C""o""r""e""N""L""P"" ""t""o"" ""b""e"" ""f""a""i""r""l""y"" ""f""a""s""t"","" ""b""u""t"" ""l""e""t""'""s"" ""c""u""t"" ""i""t"" ""s""o""m""e"" ""s""l""a""c""k""
"" "" "" "" "" "" "" "" ""#"" "" "" ""h""a""l""f"" ""a"" ""s""e""c""o""n""d"" ""p""e""r"" 