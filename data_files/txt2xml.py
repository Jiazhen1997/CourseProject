import nltk.data
import os
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.stem.porter import *
import math

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
stemmer = PorterStemmer()

text_auto = []
text_nonauto = []

print 'Processing datat in'
directory = os.path.dirname(os.path.realpath(__file__)) + '/raw_data/cleaned'
print 'dir:'+directory

for root, dirs, files in os.walk(directory):
	for file in files:	
		if file.endswith("."t"x"t"")"" ""a""n""d"" ""(""n""o""t"" ""(""'""(""1"")""'"" ""i""n"" ""f""i""l""e"")"")"" ""a""n""d"" ""(""n""o""t"" ""(""'""-""2""'"" ""i""n"" ""f""i""l""e"")"")"":""
""	""	""	""f""=""o""p""e""n""(""o""s"".""p""a""t""h"".""j""o""i""n""(""r""o""o""t"",""f""i""l""e"")"","" ""'""r""'"")""
""	""	""	""t""e""x""t""_""n""o""n""a""u""t""o"".""a""p""p""e""n""d""(""(""f""i""l""e"",""f"".""r""e""a""d""("")"")"")""
""	""	""	""f"".""c""l""o""s""e""("")""
""	""	""e""l""i""f"" ""f""i""l""e"".""e""n""d""s""w""i""t""h""(