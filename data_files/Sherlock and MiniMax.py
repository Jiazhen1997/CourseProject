

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A, P, Q = cipher
        A.sort()

        gmax = -1 << 32
        M = -1
        if P <= A[0] and gmax < A[0] - P:
            gmax = A[0] - P
            M = P
        if Q >= A[-1] and gmax < Q - A[-1]:
            gmax = Q - A[-1]
            M = Q

        for i in xrange(1, len(A)):
            max_cnd = (A[i] - A[i - 1]) / 2  
            if gmax < max_cnd:
                M_cnd = (A[i] + A[i - 1]) / 2
                if P <= M_cnd <= Q:
                    gmax = max_cnd
                    M = M_cnd

                else:  
                    if M_cnd > Q and A[i - 1] <= Q <= A[i]:
                        max_cnd = min(abs(A[i] - Q), abs(A[i - 1] - Q))
                        if gmax < max_cnd:
                            gmax = max_cnd
                            M = Q
                    if M_cnd < P and A[i - 1] <= P <= A[i]:
                        max_cnd = min(abs(A[i] - P), abs(A[i - 1] - P))
                        if gmax < max_cnd:
                            gmax = max_cnd
                            M = P
        return M


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(