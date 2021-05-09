
__author__ = 'Danyang'
MOD = 10 ** 9 + 7
BIT_CNT = 10 ** 5
SHIFT_CNT = 314159


N = BIT_CNT + SHIFT_CNT


class Solution(object):
    def solve(self, cipher):
        
        a, b = cipher
        len_a = len(a)
        len_b = len(b)

        
        a_array = [0 for _ in xrange(N)]
        b_array = [0 for _ in xrange(N)]

        
        for ind, val in enumerate(a):
            a_array[len_a - 1 - ind] = int(val)
        for ind, val in enumerate(b):
            b_array[len_b - 1 - ind] = int(val)

        
        dp = [[0, 0] for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            dp[i][0] = dp[i - 1][0] + 1 if b_array[i - 1] == 0 else dp[i - 1][0]
            dp[i][1] = dp[i - 1][1] + 1 if b_array[i - 1] == 1 else dp[i - 1][1]

        result = 0
        sig = 1
        for i in xrange(N):  
            if i < SHIFT_CNT:
                cnt_zero = dp[i + 1][0] + SHIFT_CNT - i  
                cnt_one = dp[i + 1][1]  
            else:
                cnt_zero = dp[len_b][0] - dp[i - SHIFT_CNT][0] + SHIFT_CNT  
                cnt_one = dp[len_b][1] - dp[i - SHIFT_CNT][1]  



            
            cur_bit_sum = (a_array[
                               i] ^ 0) * cnt_zero  
            cur_bit_sum += (a_array[i] ^ 1) * cnt_one

            result = (result + sig * cur_bit_sum) % MOD
            
            sig = (sig * 2) % MOD

        return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(