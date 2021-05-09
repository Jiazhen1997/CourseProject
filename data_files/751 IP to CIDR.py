

from typing import List



weights = [
    24,
    16,
    8,
    0,
]


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        
        num_ip = self.to_bin(ip)
        ret = []
        while n > 0:
            lsb = self.get_lsb(num_ip)
            while (1 << lsb) > n:
                lsb -= 1

            cur_cover = 1 << lsb
            n -= cur_cover
            ret.append(
                self.to_ip(num_ip) + f"/"{"3"2"-"l"s"b"}""
"" "" "" "" "" "" "" "" "" "" "" "" "")""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""u""m""_""i""p"" ""+""="" ""c""u""r""_""c""o""v""e""r""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""t""o""_""b""i""n""(""s""e""l""f"","" ""i""p"")"":""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""n"","" ""w"" ""i""n"" ""z""i""p""(""m""a""p""(""i""n""t"","" ""i""p"".""s""p""l""i""t""(