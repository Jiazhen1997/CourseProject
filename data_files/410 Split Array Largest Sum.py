

from typing import List
from functools import lru_cache


class SolutionDP:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        n = len(nums)
        sums = [0]
        for e in nums:
            sums.append(sums[-1] + e)

        F = [[float("i"n"f"")"" ""f""o""r"" ""_"" ""i""n"" ""r""a""n""g""e""(""m"" ""+"" ""1"")""]"" ""f""o""r"" ""_"" ""i""n"" ""r""a""n""g""e""(""n"" ""+"" ""1"")""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""r""a""n""g""e""(""1"","" ""n"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""F""[""l""]""[""1""]"" ""="" ""s""u""m""s""[""l""]"" ""-"" ""s""u""m""s""[""0""]""
"" "" "" "" "" "" "" "" ""#"" ""o""r"" ""F""[""0""]""[""0""]"" ""="" ""0""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""r""a""n""g""e""(""1"","" ""n"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""k"" ""i""n"" ""r""a""n""g""e""(""1"","" ""m"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""l"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""F""[""l""]""[""k""]"" ""="" ""m""i""n""(""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""F""[""l""]""[""k""]"","" ""m""a""x""(""F""[""j""]""[""k""-""1""]"","" ""s""u""m""s""[""l""]"" ""-"" ""s""u""m""s""[""j""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""[""n""]""[""m""]""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":""
"" "" "" "" ""d""e""f"" ""s""p""l""i""t""A""r""r""a""y""(""s""e""l""f"","" ""n""u""m""s"":"" ""L""i""s""t""[""i""n""t""]"","" ""m"":"" ""i""n""t"")"" ""-"">"" ""i""n""t"":""
"" "" "" "" "" "" "" "" 
        lo = max(nums)
        hi = sum(nums) + 1
        ret = hi
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 1  
            cur_sum = 0
            for e in nums:
                if cur_sum + e > mid:
                    cnt += 1
                    cur_sum = e
                else:
                    cur_sum += e

            if cnt <= m:
                ret = min(ret, mid)  
                hi = mid
            else:
                lo = mid + 1

        return ret


class SolutionTLE2:
    def __init__(self):
        self.sums = [0]

    def splitArray(self, nums: List[int], m: int) -> int:
        
        for n in nums:
            self.sums.append(self.sums[-1] + n)

        ret = self.dfs(len(nums), m)
        return ret

    @lru_cache(maxsize=None)
    def dfs(self, hi, m):
        
        if m == 1:
            return self.sums[hi] - self.sums[0]

        mini = float("i"n"f"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""h""i"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""i""g""h""t"" ""="" ""s""e""l""f"".""s""u""m""s""[""h""i""]"" ""-"" ""s""e""l""f"".""s""u""m""s""[""j""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t"" ""="" ""s""e""l""f"".""d""f""s""(""j"","" ""m"" ""-"" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""m""i""n""i""m""i""z""e"" ""t""h""e"" ""m""a""x""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""i""n""i"" ""="" ""m""i""n""(""m""i""n""i"","" ""m""a""x""(""l""e""f""t"","" ""r""i""g""h""t"")"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""m""i""n""i""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n""T""L""E"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""s""u""m""s"" ""="" ""[""0""]""
""
"" "" "" "" ""d""e""f"" ""s""p""l""i""t""A""r""r""a""y""(""s""e""l""f"","" ""n""u""m""s"":"" ""L""i""s""t""[""i""n""t""]"","" ""m"":"" ""i""n""t"")"" ""-"">"" ""i""n""t"":""
"" "" "" "" "" "" "" "" 
        for n in nums:
            self.sums.append(self.sums[-1] + n)
        ret = self.dfs(tuple(nums), 0, len(nums), m)
        return ret

    @lru_cache(maxsize=None)
    def dfs(self, nums, lo, hi, m):
        
        if m == 1:
            return self.sums[hi] - self.sums[lo]

        mini = float("i"n"f"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""l""o"","" ""h""i"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t"" ""="" ""s""e""l""f"".""s""u""m""s""[""j""]"" ""-"" ""s""e""l""f"".""s""u""m""s""[""l""o""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""i""g""h""t"" ""="" ""s""e""l""f"".""d""f""s""(""n""u""m""s"","" ""j"","" ""h""i"","" ""m"" ""-"" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""m""i""n""i""m""i""z""e"" ""t""h""e"" ""m""a""x""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""i""n""i"" ""="" ""m""i""n""(""m""i""n""i"","" ""m""a""x""(""l""e""f""t"","" ""r""i""g""h""t"")"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""m""i""n""i""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 