
import functools
import inspect

from typing import get_type_hints, Callable, Iterable
from collections import MutableMapping, defaultdict


OVERLOAD = "_"_"o"v"e"r"l"o"a"d"_"_""
""
""
""d""e""f"" ""g""e""t""_""k""e""y""(""i""t""r"":"" ""I""t""e""r""a""b""l""e"")"" ""-"">"" ""t""u""p""l""e"":""
"" "" "" "" ""r""e""t""u""r""n"" ""t""u""p""l""e""(""i""t""r"")""
""
""
""d""e""f"" ""d""i""s""p""a""t""c""h""(""s""e""l""f"","" ""k""e""y"","" ""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")"" ""-"">"" ""C""a""l""l""a""b""l""e"":""
"" "" "" "" ""k""e""y""_""n""e""w"" ""="" ""g""e""t""_""k""e""y""(""m""a""p""(""t""y""p""e"","" ""a""r""g""s"")"")""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""m""e""t""h""o""d"" ""="" ""s""e""l""f"".""_""_""c""l""a""s""s""_""_"".""_""_""o""v""e""r""l""o""a""d""_""_""[""k""e""y""]""[""k""e""y""_""n""e""w""]""
"" "" "" "" ""e""x""c""e""p""t"" ""K""e""y""E""r""r""o""r"":""
"" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""A""t""t""r""i""b""u""t""e""E""r""r""o""r""(access the method definition