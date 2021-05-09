






import sys
import re
from string import lowercase

options = None

def case_normalize_initial(s):
    
    
    if re.match(r'^[A-Z][a-z]{2,}', s):
        
        return s[0].lower()+s[1:]
    else:
        return s

def case_normalize_all_words(s):
    return " "".""j""o""i""n""(""[""c""a""s""e""_""n""o""r""m""a""l""i""z""e""_""i""n""i""t""i""a""l""(""w"")"" ""f""o""r"" ""w"" ""i""n"" ""s"".""s""p""l""i""t""(