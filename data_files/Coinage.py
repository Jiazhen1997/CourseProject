

__author__ = 'Danyang'


class Solution_TLE(object):
    def __init__(self):
        self.coinage = [10, 5, 2, 1]

    def solve(self, cipher):
        
        target, lst = cipher
        lst.reverse()
        result = [0]
        self.dfs(lst, target, result)
        return result[0]

    def dfs(self, seq, remaining, result):
        if remaining < 0:
            return
        if remaining == 0:
            result[0] += 1
            return

        bound = 0
        for i in xrange(4):
            bound += seq[i] * self.coinage[i]
        if bound < remaining:
            return

        for j in xrange(4):
            for i in xrange(seq[j]):
                remaining -= (i + 1) * self.coinage[j]
                self.dfs([0] * (j + 1) + seq[j + 1:], remaining, result)
                remaining += (i + 1) * self.coinage[j]


class Solution(object):
    def __init__(self):
        self.coinage = [1, 2, 5, 10]
        self.count = {}
        self.A = None

    def solve(self, cipher):
        
        target, self.A = cipher
        return self.get_count(target, 3)

    def get_count(self, n, k):
        
        if (n, k) not in self.count:
            if k == 0:
                if n % self.coinage[k] == 0 and self.coinage[k] * self.A[k] >= n:
                    self.count[(n, k)] = 1
                else:
                    self.count[(n, k)] = 0
            else:
                i = 0
                cnt = 0
                while i <= self.A[k] and i * self.coinage[k] <= n:
                    cnt += self.get_count(n - i * self.coinage[k], k - 1)
                    i += 1
                self.count[(n, k)] = cnt

        return self.count[(n, k)]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(