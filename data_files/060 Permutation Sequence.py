
import math

__author__ = 'Danyang'


class Solution(object):
    def getPermutation(self, n, k):
        k -= 1

        array = range(1, n+1)
        k %= math.factorial(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            ret.append(array.pop(idx))

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""t"")"")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""P""e""r""m""u""t""a""t""i""o""n""(""s""e""l""f"","" ""n"","" ""k"")"":""
"" "" "" "" "" "" "" "" 
        
        fac = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            fac[i] = fac[i-1]*i

        
        k -= 1  
        a = [0 for _ in xrange(n)]
        for i in xrange(n-1, -1, -1):
            a[n-1-i] = k/fac[i]  
            k %= fac[i]

        
        candidate = range(1, n+1)  
        visited = [False for _ in xrange(n)]
        for ind, val in enumerate(a):
            i = 0  
            cnt = 0  
            while True:
                if visited[i]:
                    i += 1
                else:
                    if cnt == val: break
                    cnt += 1
                    i += 1

            a[ind] = candidate[i]
            visited[i] = True

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""a"")"")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""P""e""r""m""u""t""a""t""i""o""n""_""c""o""m""p""l""i""c""a""t""e""d""(""s""e""l""f"","" ""n"","" ""k"")"":""
"" "" "" "" "" "" "" "" 
        k -= 1  

        factorial = 1  
        for i in xrange(1, n):
            factorial *= i

        result = []
        array = range(1, n+1)
        for i in reversed(xrange(1, n)):
            index = k/factorial
            result.append(array[index])
            array = array[:index]+array[index+1:]
            k = k%factorial
            factorial /= i

        
        result.append(array[0])

        return "".""j""o""i""n""(""s""t""r""(""e""l""e""m""e""n""t"")"" ""f""o""r"" ""e""l""e""m""e""n""t"" ""i""n"" ""r""e""s""u""l""t"")""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n""_""T""L""E"":""
"" "" "" "" 

    def __init__(self):
        self.counter = 0

    def getPermutation(self, n, k):
        
        if not n:
            return

        sequence = range(1, n+1)
        result = self.get_kth_permutation_dfs(sequence, k, [])
        return "".""j""o""i""n""(""s""t""r""(""e""l""e""m""e""n""t"")"" ""f""o""r"" ""e""l""e""m""e""n""t"" ""i""n"" ""r""e""s""u""l""t"")""
""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""k""t""h""_""p""e""r""m""u""t""a""t""i""o""n""_""d""f""s""(""s""e""l""f"","" ""r""e""m""a""i""n""i""n""g""_""s""e""q"","" ""k"","" ""c""u""r"")"":""
"" "" "" "" "" "" "" "" 
        if not remaining_seq:
            self.counter += 1
            if self.counter == k:
                return cur

        for ind, val in enumerate(remaining_seq):
            result = self.get_kth_permutation_dfs(remaining_seq[:ind]+remaining_seq[ind+1:], k, cur+[val])
            if result: return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""g""e""t""P""e""r""m""u""t""a""t""i""o""n""(""4"","" ""6"")"" ""=""="" 