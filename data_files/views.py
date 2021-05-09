import json
from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import SimpleTemplateResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from rake import rake


class MainView(View):
    template_name = "t"a"g"g"i"n"g"."h"t"m"l""
""
"" "" "" "" ""@""m""e""t""h""o""d""_""d""e""c""o""r""a""t""o""r""(""c""s""r""f""_""e""x""e""m""p""t"")""
"" "" "" "" ""d""e""f"" ""d""i""s""p""a""t""c""h""(""s""e""l""f"","" ""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""u""p""e""r""(""M""a""i""n""V""i""e""w"","" ""s""e""l""f"")"".""d""i""s""p""a""t""c""h""(""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""(""s""e""l""f"","" ""r""e""q""u""e""s""t"","" ""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""S""i""m""p""l""e""T""e""m""p""l""a""t""e""R""e""s""p""o""n""s""e""(""M""a""i""n""V""i""e""w"".""t""e""m""p""l""a""t""e""_""n""a""m""e"")""
""
"" "" "" "" ""d""e""f"" ""p""o""s""t""(""s""e""l""f"","" ""r""e""q""u""e""s""t"")"":""
"" "" "" "" "" "" "" "" ""d""i""c"" ""="" ""j""s""o""n"".""l""o""a""d""s""(""r""e""q""u""e""s""t"".""b""o""d""y"")""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""r""a""k""e"".""R""a""k""e""("")"".""r""u""n""(""d""i""c""[