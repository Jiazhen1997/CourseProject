

MOD = 10 ** 9 + 7
__author__ = 'Danyang'


class Solution_error(object):
    def solve(self, cipher):
        
        L = [cipher[2 * i] for i in xrange(4)]
        R = [cipher[2 * i + 1] for i in xrange(4)]

        result = 1
        for i in xrange(4):
            result = (result * (R[i] - L[i] + 1)) % MOD

        pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
        for pair in pairs:
            other = max(0, min(R[i] for i in pair) - max(L[i] for i in pair) + 1)
            for i in xrange(4):
                if i not in pair:
                    other = (other * (R[i] - L[i] + 1)) % MOD
            result = (result - other) % MOD

        pairs = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
        for pair in pairs:
            other = max(0, min(R[i] for i in pair) - max(L[i] for i in pair) + 1)
            for i in xrange(4):
                if i not in pair:
                    other = (other * (R[i] - L[i] + 1)) % MOD
            result = (result + other) % MOD

        result = (result - max(0, min(R) - max(L) + 1)) % MOD
        return result


class Interval(object):
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def card(self):
        if self.is_empty():
            return 0
        return self.r - self.l + 1

    def intersect(self, other):
        if self.is_empty() or other.is_empty():
            return Interval(0, -1)

        l = max(self.l, other.l)
        r = min(self.r, other.r)
        return Interval(l, r)

    def is_empty(self):
        return self.l > self.r


class Solution(object):
    def solve(self, cipher):
        

        R = [Interval(cipher[2 * i], cipher[2 * i + 1]) for i in xrange(4)]

        w0 = 0
        w0 += R[0].card() * R[1].card() * R[2].card() * R[3].card()
        w0 %= MOD

        w1 = 0
        for i in xrange(4):
            w1 += R[i % 4].intersect(R[(i + 1) % 4]).card() * R[(i + 2) % 4].card() * R[(i + 3) % 4].card()
            w1 %= MOD

        w2 = 0
        for i in xrange(4):
            w2 += R[i % 4].intersect(R[(i + 1) % 4]).intersect(R[(i + 2) % 4]).card() * R[(i + 3) % 4].card()
            w2 %= MOD

        for i in xrange(2):
            w2 += R[i % 4].intersect(R[(i + 1) % 4]).card() * R[(i + 2) % 4].intersect(R[(i + 3) % 4]).card()
            w2 %= MOD

        w3 = 0
        for i in xrange(4):
            w3 += R[i % 4].intersect(R[(i + 1) % 4]).intersect(R[(i + 2) % 4]).intersect(R[(i + 3) % 4]).card()
            w3 %= MOD

        w4 = 0
        w4 += R[0].intersect(R[1]).intersect(R[2]).intersect(R[3]).card()
        w4 %= MOD

        return (w0 - w1 + w2 - w3 + w4) % MOD


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(