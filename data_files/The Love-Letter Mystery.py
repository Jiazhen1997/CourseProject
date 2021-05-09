
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        start_ptr = 0
        end_ptr = len(cipher) - 1

        cnt = 0
        while start_ptr < end_ptr:
            ord1 = ord(cipher[start_ptr]) - ord('a')
            ord2 = ord(cipher[end_ptr]) - ord('a')
            cnt += abs(ord1 - ord2)
            start_ptr += 1
            end_ptr -= 1

        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(