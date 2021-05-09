import os
import re






entities = ['Ingredient','Amount','Unit','Recipe']
auto_tag_set = []
nonauto_tag_set = []

def init_dict(dictOfdict):
	for e in entities:
		if not (e in dictOfdict):
			dictOfdict[e] = dict()

def get_xml_content(file_path):
	f = open(file_path)
	content = f.read()
	content = pre_format(content)
	return get_xml_entity(content)

def get_ann_content(file_path):
	f = open(file_path)
	content = f.read()
	return get_ann_entity(content)

def process_files_in_dir(dir):
	dir = os.path.dirname(os.path.realpath(__file__)) + ('/'+dir)
	for root, dirs, files in os.walk(dir):
		for file in sorted(files):
			if(file.endswith('.xml')):
				auto_tag_set.append(get_xml_content(os.path.join(root,file)))
			if(file.endswith('.ann')):
				nonauto_tag_set.append(get_ann_content(os.path.join(root,file)))

def get_ann_entity(content):
	entity_dict = dict()
	init_dict(entity_dict)
	content = content.split('\n')
	for line in content:
		token = line.split('\t')
		if("T"" ""i""n"" ""t""o""k""e""n""[""0""]"")"":""
""	""	""	""t""a""g""_""n""a""m""e"" ""="" ""t""o""k""e""n""[""1""]"".""s""p""l""i""t""(""'"" ""'"")""[""0""]""
""	""	""	""i""f""(""t""o""k""e""n""[""2""]"" ""i""n"" ""e""n""t""i""t""y""_""d""i""c""t""[""t""a""g""_""n""a""m""e""]"")"":""
""	""	""	""	""e""n""t""i""t""y""_""d""i""c""t""[""t""a""g""_""n""a""m""e""]""[""t""o""k""e""n""[""2""]""]"" ""+""="" ""1""
""	""	""	""e""l""s""e"":""
""	""	""	""	""e""n""t""i""t""y""_""d""i""c""t""[""t""a""g""_""n""a""m""e""]""[""t""o""k""e""n""[""2""]""]"" ""="" ""1""
""	""r""e""t""u""r""n"" ""e""n""t""i""t""y""_""d""i""c""t""
""
""
""d""e""f"" ""g""e""t""_""x""m""l""_""e""n""t""i""t""y""(""c""o""n""t""e""n""t"")"":""
""	""e""n""t""i""t""y""_""d""i""c""t"" ""="" ""d""i""c""t""("")""
""	""i""n""i""t""_""d""i""c""t""(""e""n""t""i""t""y""_""d""i""c""t"")""
""	""f""o""r"" ""e"" ""i""n"" ""e""n""t""i""t""i""e""s"":""
""	""	""e""_""r""e""g"" ""="" ""r""e"".""c""o""m""p""i""l""e""(""'""<""'""+""e"" ""+"" ""'"">""(""?""P""<""'""+""e""+""'"">""[""^""<""]""+"")""<""/""'""+""e""+""'"">""'"")"";""
""	""	""f""o""r"" ""i"" ""i""n"" ""e""_""r""e""g"".""f""i""n""d""a""l""l""(""c""o""n""t""e""n""t"")"":""
""	""	""	""i""f""(""i"" ""i""n"" ""e""n""t""i""t""y""_""d""i""c""t""[""e""]"")"":""
""	""	""	""	""e""n""t""i""t""y""_""d""i""c""t""[""e""]""[""i""]"" ""+""="" ""1""
""	""	""	""e""l""s""e"":""
""	""	""	""	""e""n""t""i""t""y""_""d""i""c""t""[""e""]""[""i""]"" ""="" ""1""
""	""r""e""t""u""r""n"" ""e""n""t""i""t""y""_""d""i""c""t""
""
""d""e""f"" ""p""r""e""_""f""o""r""m""a""t""(""c""o""n""t""e""n""t"")"":""
""
""	""#""f""o""r"" ""n""o""n""-""a""u""t""o""
""	""c""o""n""t""e""n""t"" ""="" ""r""e"".""s""u""b""(