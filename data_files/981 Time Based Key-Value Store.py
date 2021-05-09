

import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        n = (timestamp, value)
        bisect.insort(self.m[key], n)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
""
"" "" "" "" "" "" "" "" ""#"" ""f""i""n""d"" ""t""h""e"" ""l""a""r""g""e""s""t"" ""v"","" ""s"".""t""."" ""v"" ""<""="" ""t""
"" "" "" "" "" "" "" "" ""l""s""t"" ""="" ""s""e""l""f"".""m""[""k""e""y""]""
"" "" "" "" "" "" "" "" ""i"" ""="" ""b""i""s""e""c""t"".""b""i""s""e""c""t""(""l""s""t"","" ""(""t""i""m""e""s""t""a""m""p"","" 