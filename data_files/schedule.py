from collections import defaultdict

__author__ = 'Daniel'


class Val(object):
    def __init__(self):
        self.cnt = 0
        self.start = 0


class TaskScheduleSolution(object):
    def solve(self, A, intvl):
        m = defaultdict(Val)
        for e in A:
            m[e].cnt += 1

        t = 0  
        for _ in A:
            maxa = None
            for k, v in m.items():
                if not maxa or m[maxa].cnt <= v.cnt:
                    if m[maxa].cnt == v.cnt and m[maxa].start > v.start:
                        maxa = k
                    elif m[maxa].cnt < v.cnt:
                        maxa = k

            
            t = max(t, m[maxa].start)+1
            m[maxa].cnt -= 1
            if m[maxa] <= 0:
                del m[maxa]

            m[maxa].start = t+intvl

        return t


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""T""a""s""k""S""c""h""e""d""u""l""e""S""o""l""u""t""i""o""n""("")"".""s""o""l""v""e""(""[""1"","" ""1"","" ""2"","" ""1""]"","" ""2"")"" ""=""="" ""7""
"" "" "" "" ""a""s""s""e""r""t"" ""T""a""s""k""S""c""h""e""d""u""l""e""S""o""l""u""t""i""o""n""("")"".""s""o""l""v""e""(""[""1"","" ""2"","" ""3"","" ""1"","" ""2"","" ""3""]"","" ""3"")"" ""=""="" ""7""
