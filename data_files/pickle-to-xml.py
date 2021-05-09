








import pickle
import os
import codecs

def dump_pickles(out, dirname, filename, path):
    f = open(os.path.join(dirname, filename), 'r')
    data = pickle.load(f)
    fragment_file = codecs.open(data['current_page_name'] + '.frag', mode='w', encoding='utf-8')
    fragment_file.write(data['body'])
    fragment_file.close()
    out.write('  <page url="%"s"">""\""n""'"" ""%"" ""p""a""t""h"")""
"" "" "" "" ""o""u""t"".""w""r""i""t""e""(""'"" "" "" "" ""<""f""r""a""g""m""e""n""t"">""%""s"".""f""r""a""g""<""/""f""r""a""g""m""e""n""t"">""\""n""'"" ""%"" ""d""a""t""a""[""'""c""u""r""r""e""n""t""_""p""a""g""e""_""n""a""m""e""'""]"")""
"" "" "" "" ""i""f"" ""d""a""t""a""[""'""p""r""e""v""'""]"" ""i""s"" ""n""o""t"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" ""o""u""t"".""w""r""i""t""e""(""'"" "" "" "" ""<""p""r""e""v"" ""u""r""l""=