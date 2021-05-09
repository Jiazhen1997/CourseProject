
import sys

__author__ = 'Danyang'


class Solution(object):
    def minWindow(self, S, T):
        
        min_win = [0, sys.maxint]  
        w_cnt = [0 for _ in range(256)]  
        t_cnt = [0 for _ in range(256)]  
        for char in T:
            t_cnt[ord(char)] += 1

        appeared_cnt = 0
        lo = 0
        for hi in xrange(1, len(S)+1):
            
            val = S[hi-1]
            if t_cnt[ord(val)] > 0:
                w_cnt[ord(val)] += 1

            if t_cnt[ord(val)] > 0 and w_cnt[ord(val)] <= t_cnt[ord(val)]:
                appeared_cnt += 1  

            
            if appeared_cnt == len(T):  
                while w_cnt[ord(S[lo])] > t_cnt[ord(S[lo])] or t_cnt[ord(S[lo])] == 0:
                    if w_cnt[ord(S[lo])] > 0: w_cnt[ord(S[lo])] -= 1
                    lo += 1

                if min_win[1]-min_win[0] > hi-lo:
                    min_win[0], min_win[1] = lo, hi

        if min_win[1] == sys.maxint:
            return ""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""S""[""m""i""n""_""w""i""n""[""0""]"":""m""i""n""_""w""i""n""[""1""]""]""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 