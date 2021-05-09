



class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        
        t = 0
        while Y > X:
            if Y % 2 == 0:
                Y //= 2
            else:
                Y += 1
            t += 1

        return t + X - Y

    def brokenCalc_TLE(self, X: int, Y: int) -> int:
        
        q = [X]
        t = 0
        has_larger = False
        while q:
            cur_q = []
            for e in q:
                if e == Y:
                    return t

                cur = e * 2
                if cur >= 1:
                    if cur > Y and not has_larger:
                        has_larger = True
                        cur_q.append(cur)
                    elif cur <= Y:
                        cur_q.append(cur)

                cur = e - 1
                if cur >= 1:
                    cur_q.append(cur)
            q = cur_q
            t += 1

        raise


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""b""r""o""k""e""n""C""a""l""c""(""2"","" ""3"")"" ""=""="" ""2""
