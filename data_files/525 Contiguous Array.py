



class Solution:
    def findMaxLength(self, nums):
        
        o = 0
        z = 0
        d = {0: 0}  
        ret = 0
        for i, e in enumerate(nums):
            if e == 1:
                o += 1
            else:
                z += 1
            diff = o - z
            if diff in d:
                ret = max(ret, i + 1 - d[diff])
            else:
                d[diff] = i + 1

        return ret

    def findMaxLength_error(self, nums):
        
        n = len(nums)
        F = [0 for _ in range(n+1)]
        for i in range(n):
            F[i+1] = F[i]
            if nums[i] == 0:
                F[i+1] += 1

        i = 0
        j = n
        while i < j:
            count = F[j] - F[i]
            l = j - i
            if count * 2 == l:
                print(l)
                return l
            elif count * 2 < l:
                if nums[i] == 1:
                    i += 1
                else:
                    j -= 1
            else:
                if nums[i] == 0:
                    i += 1
                else:
                    j -= 1
        return 0


    def findMaxLength_TLE(self, nums):
        
        F = [0]
        n = len(nums)
        for e in nums:
            if e == 0:
                F.append(F[-1] + 1)
            else:
                F.append(F[-1])

        ret = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if (F[j] - F[i]) * 2 == j - i:
                    ret = max(ret, j - i)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""a""x""L""e""n""g""t""h""(""[""0"","" ""1"","" ""0""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""a""x""L""e""n""g""t""h""(""[""0"",""1"",""0"",""1"",""1"",""1"",""0"",""0"",""1"",""1"",""0"",""1"",""1"",""1"",""1"",""1"",""1"",""0"",""1"",""1"",""0"",""1"",""1"",""0"",""0"",""0"",""1"",""0"",""1"",""0"",""0"",""1"",""0"",""1"",""1"",""1"",""1"",""1"",""1"",""0"",""0"",""0"",""0"",""1"",""0"",""0"",""0"",""1"",""1"",""1"",""0"",""1"",""0"",""0"",""1"",""1"",""1"",""1"",""1"",""0"",""0"",""1"",""1"",""1"",""1"",""0"",""0"",""1"",""0"",""1"",""1"",""0"",""0"",""0"",""0"",""0"",""0"",""1"",""0"",""1"",""0"",""1"",""1"",""0"",""0"",""1"",""1"",""0"",""1"",""1"",""1"",""1"",""0"",""1"",""1"",""0"",""0"",""0"",""1"",""1""]"")"" ""=""="" ""6""8""
