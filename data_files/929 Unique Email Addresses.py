

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        s = set()
        for e in emails:
            local, domain = e.split("@"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""o""c""a""l"" ""="" ""s""e""l""f"".""s""t""e""m""(""l""o""c""a""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"".""a""d""d""(""(""l""o""c""a""l"","" ""d""o""m""a""i""n"")"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""l""e""n""(""s"")""
""
"" "" "" "" ""d""e""f"" ""s""t""e""m""(""s""e""l""f"","" ""l""o""c""a""l"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""l""o""c""a""l"".""s""p""l""i""t""(