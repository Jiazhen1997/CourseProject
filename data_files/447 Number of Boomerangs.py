

from collections import Counter


class Solution:
    def distance(self, a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2

    def numberOfBoomerangs(self, points):
        
        ret = 0
        for i in range(len(points)):
            dist_cnt = Counter()
            for j in range(len(points)):
                if i != j:
                    d = self.distance(points[i], points[j])
                    dist_cnt[d] += 1

            for v in dist_cnt.values():
                
                ret += v * (v - 1)

        return ret

    def numberOfBoomerangs_TLE(self, points):
        
        ret = 0
        for i in range(len(points)):
            dist_cnt = Counter()
            dist_lst = []
            for j in range(len(points)):
                if i != j:
                    d = self.distance(points[i], points[j])
                    dist_lst.append(d)
                    dist_cnt[d] += 1

            for d in dist_lst:
                ret += (dist_cnt[d] - 1)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""b""e""r""O""f""B""o""o""m""e""r""a""n""g""s""(""[""[""0"",""0""]"",""[""1"",""0""]"",""[""2"",""0""]""]"")"" ""=""="" ""2""
