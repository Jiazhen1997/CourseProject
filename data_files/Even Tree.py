
__author__ = 'Danyang'


class Solution(object):
    def __init__(self, N, M):
        self.f = [0 for _ in xrange(N + 1)]  
        self.V = [[] for _ in xrange(N + 1)]  
        self.E = []

    def solve(self, cipher):
        
        N, M, E = cipher
        for e in E:
            u, v = e
            self.E.append([u, v])
            self.V[u].append(v)
            self.V[v].append(u)

        self.get_sum(1, 0)

        result = 0
        for i in xrange(2, N + 1):  
            if self.f[i] % 2 == 0:
                result += 1
        return result

    def get_sum(self, cur, pi):
        
        if self.f[cur] == 0:
            for nigh in self.V[cur]:
                if nigh != pi:
                    self.f[cur] += self.get_sum(nigh, cur)  

            self.f[cur] += 1  

        return self.f[cur]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(