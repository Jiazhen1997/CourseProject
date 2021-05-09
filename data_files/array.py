from collections import deque
__author__ = 'Daniel'


class MaxProductSolution(object):
    def solve(self, A):
        
        q = deque([A[0]])
        maxa = 0
        for e in A[1:]:
            while q and q[0] < e:
                maxa = max(maxa, q[0]*e)
                q.popleft()

            q.append(e)

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""M""a""x""P""r""o""d""u""c""t""S""o""l""u""t""i""o""n""("")"".""s""o""l""v""e""(""[""1"","" ""6"","" ""2"","" ""3"","" ""6"","" ""4"","" ""9"","" ""5"","" ""1""0""]"")"" ""=""="" ""9""0