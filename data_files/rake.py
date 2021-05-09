





import re
import operator
import os

BASE_DIR = (os.path.dirname(os.path.abspath(__file__)))

debug = False


def is_number(s):
    try:
        float(s) if '.' in s else int(s)
        return True
    except ValueError:
        return False


def load_stop_words(stop_word_file):
    
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""w""o""r""d"" ""i""n"" ""l""i""n""e"".""s""p""l""i""t""("")"":"" "" ""#"" ""i""n"" ""c""a""s""e"" ""m""o""r""e"" ""t""h""a""n"" ""o""n""e"" ""p""e""r"" ""l""i""n""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""o""p""_""w""o""r""d""s"".""a""p""p""e""n""d""(""w""o""r""d"")""
"" "" "" "" ""r""e""t""u""r""n"" ""s""t""o""p""_""w""o""r""d""s""
""
""
""d""e""f"" ""s""e""p""a""r""a""t""e""_""w""o""r""d""s""(""t""e""x""t"","" ""m""i""n""_""w""o""r""d""_""r""e""t""u""r""n""_""s""i""z""e"")"":""
"" "" "" "" 
    splitter = re.compile(r'[^a-zA-Z0-9_\+\-/]')
    words = []
    for single_word in splitter.split(text):
        current_word = single_word.strip().lower()
        
        if len(current_word) > min_word_return_size and current_word != '' and not is_number(current_word):
            words.append(current_word)
    return words


def split_sentences(text):
    
    sentence_delimiters = re.compile(r'[!\?;:\[\]\t\"\"("\")"]"|"\"s"\"-"\"s"|"["^"0"-"9"]","["^"a"-"z"A"-"Z"0"-"9"]"|"\"."["^"a"-"z"A"-"Z"0"-"9"]"|"\"."$"'")"
" " " " "s"e"n"t"e"n"c"e"s" "=" "s"e"n"t"e"n"c"e"_"d"e"l"i"m"i"t"e"r"s"."s"p"l"i"t"("t"e"x"t")"
" " " " "r"e"t"u"r"n" "s"e"n"t"e"n"c"e"s"
"
"
"d"e"f" "b"u"i"l"d"_"s"t"o"p"_"w"o"r"d"_"r"e"g"e"x"("s"t"o"p"_"w"o"r"d"_"f"i"l"e"_"p"a"t"h")":"
" " " " "s"t"o"p"_"w"o"r"d"_"l"i"s"t" "=" "l"o"a"d"_"s"t"o"p"_"w"o"r"d"s"("s"t"o"p"_"w"o"r"d"_"f"i"l"e"_"p"a"t"h")"
" " " " "s"t"o"p"_"w"o"r"d"_"r"e"g"e"x"_"l"i"s"t" "=" "["]"
" " " " "f"o"r" "w"o"r"d" "i"n" "s"t"o"p"_"w"o"r"d"_"l"i"s"t":"
" " " " " " " " "w"o"r"d"_"r"e"g"e"x" "=" "r"'"\"b"'"+"w"o"r"d"+"r"'"("?"!"["\"w"-"]")"'" " "#" "a"d"d"e"d" "l"o"o"k" "a"h"e"a"d" "f"o"r" "h"y"p"h"e"n"
" " " " " " " " "s"t"o"p"_"w"o"r"d"_"r"e"g"e"x"_"l"i"s"t"."a"p"p"e"n"d"("w"o"r"d"_"r"e"g"e"x")"
" " " " "s"t"o"p"_"w"o"r"d"_"p"a"t"t"e"r"n" "=" "r"e"."c"o"m"p"i"l"e"("'"|"'"."j"o"i"n"("s"t"o"p"_"w"o"r"d"_"r"e"g"e"x"_"l"i"s"t")"," "r"e"."I"G"N"O"R"E"C"A"S"E")"
" " " " "r"e"t"u"r"n" "s"t"o"p"_"w"o"r"d"_"p"a"t"t"e"r"n"
"
"
"d"e"f" "g"e"n"e"r"a"t"e"_"c"a"n"d"i"d"a"t"e"_"k"e"y"w"o"r"d"s"("s"e"n"t"e"n"c"e"_"l"i"s"t"," "s"t"o"p"w"o"r"d"_"p"a"t"t"e"r"n")":"
" " " " "p"h"r"a"s"e"_"l"i"s"t" "=" "["]"
" " " " "f"o"r" "s" "i"n" "s"e"n"t"e"n"c"e"_"l"i"s"t":"
" " " " " " " " "t"m"p" "=" "r"e"."s"u"b"("s"t"o"p"w"o"r"d"_"p"a"t"t"e"r"n"," "'"|"'"," "s"."s"t"r"i"p"(")")"
" " " " " " " " "p"h"r"a"s"e"s" "=" "t"m"p"."s"p"l"i"t"(""|