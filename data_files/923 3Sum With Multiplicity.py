

from typing import List
from collections import defaultdict


MOD = 10 ** 9 + 7


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        
        counter = defaultdict(int)
        for a in A:
            counter[a] += 1

        keys = list(counter.keys())
        keys.sort()
        n = len(keys)
        ret = 0
        for i in range(n):
            j = i  
            k = n - 1
            while j <= k:  
                a, b, c = keys[i], keys[j], keys[k]
                if b + c < target - a:
                    j += 1
                elif b + c > target - a:
                    k -= 1
                else:  
                    if a < b < c:
                        ret += counter[a] * counter[b] * counter[c]
                    elif a == b < c:
                        
                        ret += counter[a] * (counter[a] - 1) // 2 * counter[c]
                    elif a < b == c:
                        ret += counter[a] * counter[b]  * (counter[b] - 1) // 2
                    elif a== b == c:
                        
                        ret += counter[a] * (counter[a] - 1) * (counter[a] - 2) // (3 * 2)
                    else:
                        raise

                    ret %= MOD
                    j += 1
                    k -= 1

        return ret

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        
        A.sort()
        n = len(A)
        ret = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                if A[j] + A[k] < target - A[i]:
                    j += 1
                elif A[j] + A[k] > target - A[i]:
                    k -= 1
                else:  
                    l_cnt = 1
                    while j + l_cnt < n and A[j + l_cnt] == A[j]:
                        l_cnt += 1

                    r_cnt = 1
                    while k - r_cnt >= 0 and A[k - r_cnt] == A[k]:
                        r_cnt += 1

                    if A[j] != A[k]:
                        ret += l_cnt * r_cnt
                        ret %= MOD
                    else:
                        ret += l_cnt * (l_cnt - 1) // 2  
                        ret %= MOD

                    j += l_cnt
                    k -= r_cnt

        return ret

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        
        n = len(A)
        F = [[[0 for _ in range(3 + 1)] for _ in range(target + 1)] for _ in range(n+1)]

        for i in range(n+1):
            F[i][0][0] = 1

        for i in range(1, n + 1):
            for t in range(target + 1):
                for k in range(1, 3 + 1):
                    
                    F[i][t][k] = F[i-1][t][k] % MOD
                    if t - A[i-1] >= 0:
                        F[i][t][k] += F[i-1][t-A[i-1]][k-1] % MOD

        print(F[n][target][3])
        return F[n][target][3]

    def threeSumMulti_TLE(self, A: List[int], target: int) -> int:
        
        F = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        n = len(A)
        for i in range(n+1):
            F[i][0][0] = 1

        for i in range(1, n + 1):
            for t in range(target + 1):
                for k in range(1, 3 + 1):
                    
                    F[i][t][k] = F[i-1][t][k] + F[i-1][t-A[i-1]][k-1]
                    F[i][t][k] %= MOD

        return F[n][target][3]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""r""e""e""S""u""m""M""u""l""t""i""(""[""1"",""1"",""2"",""2"",""3"",""3"",""4"",""4"",""5"",""5""]"","" ""8"")"" ""=""="" ""2""0""
