

from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        
        ret = 0
        i_lo, i_hi, j = 0, 0, 0
        sum_lo, sum_hi = 0, 0
        for j in range(len(A)):
            sum_lo += A[j]
            sum_hi += A[j]
            while i_lo < j and sum_lo > S:
                sum_lo -= A[i_lo]
                i_lo += 1
            while i_hi < j and (sum_hi > S or sum_hi == S and A[i_hi] == 0):
                sum_hi -= A[i_hi]
                i_hi += 1
            assert i_hi >= i_lo
            if sum_lo == S:
                assert sum_hi == S
                ret += i_hi - i_lo + 1

        return ret

    def numSubarraysWithSum_error(self, A: List[int], S: int) -> int:
        
        ret = 0
        i = 0
        j = 0
        n = len(A)
        cur_sum = 0
        while j < n:
            cur_sum += A[j]
            if cur_sum < S and j < n:
                j += 1
            elif cur_sum == S:
                ret += 1
                while i <= j and A[i] == 0:
                    i += 1
                    ret += 1
                j += 1
            else:
                while i <= j and cur_sum > S:
                    cur_sum -= A[i]
                    i += 1
                if cur_sum == S:
                    ret += 1
                    while i <= j and A[i] == 0:
                        i += 1
                        ret += 1
                j += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""S""u""b""a""r""r""a""y""s""W""i""t""h""S""u""m""(""[""1"",""0"",""1"",""0"",""1""]"","" ""2"")"" ""=""="" ""4""
