
__author__ = 'Daniel'


class Solution(object):
    def numbersByRecursion(self, n):
        return self.rec(n)

    def rec(self, n):
        if n == 0:
            return []
        if n == 1:
            return [i+1 for i in xrange(9)]
        else:
            lst = self.rec(n-1)
            l = len(lst)
            cur = []
            prev = lst[-1]+1
            for i in xrange(prev-prev/10):
                for j in xrange(10):
                   cur.append(lst[prev/10-1+i]*10+j)

            lst.extend(cur)
            return lst

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""b""e""r""s""B""y""R""e""c""u""r""s""i""o""n""(""2"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""b""e""r""s""B""y""R""e""c""u""r""s""i""o""n""(""2"")"" ""=""="" ""[""i""+""1"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""9""9"")""]