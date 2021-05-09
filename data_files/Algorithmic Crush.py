
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M, queries = cipher

        qry = []
        for query in queries:
            qry.append((query[0], query[2]))
            qry.append((query[1] + 1, -query[2]))

        qry.sort(key=lambda x: (x[0], x[1]))
        

        maxa = -1 << 32
        cur = 0
        for q in qry:
            cur += q[1]
            maxa = max(maxa, cur)

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(