
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        


    def solve_time_out(self, cipher):
        
        A = cipher
        L = [-1 for _ in A]
        S = [-1 for _ in A]
        for i in xrange(len(A) - 2, -1, -1):
            idx = i + 1
            while idx != -1:
                if A[idx] < A[i]:
                    idx = L[idx]
                else:
                    break
            L[i] = idx

            idx = i + 1
            while idx != -1:
                if A[idx] > A[i]:
                    idx = S[idx]
                else:
                    break
            S[i] = idx

        cnt = 0
        for i in xrange(len(A)):
            cnt += 1
            l = L[i]
            s = S[i]
            while l != -1 and (s == -1 or s > l):
                cnt += 1
                l = L[l]

        return cnt

    def solve_error(self, cipher):
        
        A = cipher
        N = len(A)
        start = 0
        end = 1  
        cnt = 0
        while end < N:
            if A[end] > A[end - 1]:
                end += 1
            else:
                cnt += self.count(start, end)
                start = end
                end += 1

        cnt += self.count(start, end)
        return cnt

    def count(self, start, end):
        l = end - start
        return (l + 1) * l / 2


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(