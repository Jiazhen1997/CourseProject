import re
from django.http import HttpResponse

def json_only(func):
  def ret(*args, **kwargs):
    request = args[0]
    if (request.is_ajax() and
            re.match(r"a"p"p"l"i"c"a"t"i"o"n"/"j"s"o"n"","" ""r""e""q""u""e""s""t"".""M""E""T""A""[