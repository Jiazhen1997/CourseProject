

__author__ = 'Danyang'
MOD = 1e9 + 7


class Solution(object):
    def solve_TLE(self, cipher):
        
        A = map(int, list(cipher))
        f = A[0]
        num = A[0]
        sig = 1
        for i in xrange(1, len(A)):
            num = 10 * num + A[i]
            sig *= 10

            temp = num
            temp_sig = sig
            while temp_sig >= 1:
                f += temp
                f %= MOD

                temp %= temp_sig
                temp_sig /= 10

        return int(f)

    def solve(self, cipher):
        
        pre = [0 for _ in cipher]
        pre[0] = int(cipher[0])
        for i in xrange(1, len(cipher)):
            pre[i] = (pre[i - 1] * 10 + int(cipher[i]) * (i + 1)) % MOD

        s = 0
        for elt in pre:
            s = (s + elt) % MOD

        return int(s)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(